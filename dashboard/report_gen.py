import io, os, datetime as dt
from datetime import datetime, timedelta
from dashboard.models import PersonResponsible
from .views import DashboardModel
from django.conf import settings
from django.http import HttpResponse
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm, cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, Image, Frame, KeepInFrame, Spacer
from reportlab.lib.colors import *
from reportlab.lib.enums import *
from reportlab.lib.utils import ImageReader


class Report:

    def __init__(self, filename, uuid):   
        self.filename = filename  
        self.uuid = uuid
        self.pagesize = A4
        self.width, self.height = self.pagesize
        self.buffer = io.BytesIO()
        self.styles = getSampleStyleSheet()
        self.c = self.createCanvas(self.buffer)
        self.record = DashboardModel.objects.get(id=uuid) #obtain context for the primary key
      #  print("test...", self.record.id)


    def createCanvas(self, buffer):           
        myCanvas = canvas.Canvas(buffer, self.pagesize, bottomup=0)
        return myCanvas


    def getBuffer(self):  
        self.page_one(pagenumber=1) 
        self.page_two(pagenumber=2) 
        self.page_three(pagenumber=3) 
        self.page_four(pagenumber=4) 
        self.c.save() #save the canvas
        self.buffer.seek(0)
       
        return self.buffer

    
    def generate(request, pk, param):
        meta = DashboardModel.objects.get(pk=pk)
        doc = Report(filename=str(meta.ncr_number), uuid=pk)
        response = HttpResponse()
        response.content = doc.getBuffer()
        response.headers['pk'] = pk
        response.headers['Url-param'] = param
        response.headers['Content-Disposition'] = 'inline; filename=' + doc.filename + ".pdf"
        response.headers['Content-Type'] = 'application/pdf'

        return response


    def includeFooter(self, pageNumber):                
        footer_line_h = self.height-60   
        self.c.line(cm, footer_line_h, self.width - inch + 1.05*cm, footer_line_h) 
        self.c.setFont("Times-Roman", 8)    
        self.c.drawString(1.1*cm, footer_line_h+10, "Report:")
        self.c.drawString(inch, footer_line_h+10, "NCR Report")
       # self.c.drawString(4.5*inch+cm, footer_line_h+10, "https://github.com/Sphaze/")
        self.c.drawString(7*inch+7*mm, footer_line_h+10, "Page %d" % pageNumber)



    def page_one(self, pagenumber): 

        # the_issue_date = str(self.record.issue_date)[8:10] +'/'+str(self.record.issue_date)[5:7] +'/'+str(self.record.issue_date)[0:4]  
        # the_issue_time = str(self.record.issue_date)[10:16]

        # theHour = int(the_issue_time[:3]) + 1
        # theMinutes = the_issue_time[4:6]
        # the_issue_time_ = "{:02d}".format(theHour) + ':' + theMinutes

        # https://docs.python.org/3/library/datetime.html
        # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
        # https://docs.python.org/3/library/datetime.html#datetime.timedelta
        # https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo

        UTC_time_format = "%Y-%m-%d %H:%M:%S"
        UTC_date_format = "%Y-%m-%d"
        custom_time_format = "%d/%m/%Y %H:%M"
        custom_date_format = "%d/%m/%Y"

        the_issue_datetime = ""
        the_closure_date = ""
        the_target_completion_date = ""

        if(self.record.issue_date):
            timestring = datetime.strptime(str(self.record.issue_date + timedelta(hours=1))[:19], UTC_time_format)
            the_issue_datetime = datetime.fromtimestamp(timestring.timestamp()).__format__(custom_time_format)
            the_issue_datetime = str(the_issue_datetime)
        else:
            the_issue_datetime = "Please update the record with the time and date of the issue"

        if(self.record.closure_date):
            timestring = datetime.strptime(str(self.record.closure_date)[:10], UTC_date_format)
            the_closure_date = datetime.fromtimestamp(timestring.timestamp()).__format__(custom_date_format)
            the_closure_date = str(the_closure_date)
        else:
            the_closure_date = ""

        if(self.record.target_completion_date):
            timestring = datetime.strptime(str(self.record.target_completion_date)[:10], UTC_date_format)
            the_target_completion_date = datetime.fromtimestamp(timestring.timestamp()).__format__(custom_date_format)
            the_target_completion_date = str(the_target_completion_date)
        else:
            the_target_completion_date = ""

        logo = os.path.join(settings.STATIC_ROOT,"img/logo.jpg")       
        logoX = (self.width/2) + 2*inch + 1*mm
        logoY = 2 * inch
        logoSize = 115
        self.c.saveState()
        self.c.scale(1,-1)
        self.c.drawImage(logo, width=logoSize, x=logoX, y=-logoY, preserveAspectRatio=True)
        self.c.restoreState()


        lineStart = 1*cm
        lineEnd = self.width - inch + 1.05*cm
        line_Y = 2*inch - 20
   
        self.c.line(lineStart, line_Y, lineEnd, line_Y)

        '''set fonts for text blobs''' 

        heading_font = "Helvetica"
        heading_fontsize = 9
        answer_font = "Helvetica-Bold"
        answer_fontsize = 11
    
        ### left column ###
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Report:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+0.5*cm+2*mm)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("NCR Report")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+1.5*cm)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Advice Number:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+2*cm+2*mm)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine(self.record.advice_number)
        self.c.drawText(textobject)
        
        q_engineers_list = [str(name) for name in self.record.printed_by.all()]
        quality_engineers = ', '.join(q_engineers_list)

        ### center column ###
        ''' heading blob '''  
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Printed by:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+0.5*cm+2*mm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine(quality_engineers)
        self.c.drawText(textobject)

        supervisors_list = [str(name) for name in self.record.supervisor.all()]
        the_supervisors = ', '.join(supervisors_list)

        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+1.5*cm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Created by:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+2*cm+2*mm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine(the_supervisors)
        self.c.drawText(textobject)

        ### right column ###
        
        ''' heading blob '''  
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Execution time:")
        #textobject.textLine("Issue time:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+0.5*cm+2*mm)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        execution_time = str(dt.datetime.now().__format__("%d/%m/%Y %H:%M"))
        textobject.textLine(execution_time)
        self.c.drawText(textobject)
   

        #data = Post.objects.last() #most recent database object from my database model called "Post"
        
        '''heading fields'''
        a1 = "NCR ID:"
        a2 = "Date of NCR:"
        a3 = "Advice Number:"
        a4 = "Status:"
        a5 = "Area:"
        a6 = "Area in specific:"
        a7 = "Severity:"
        a8 = "Responsible for the issue:"
        a9 = "Category:"
        a10 = "Company:"
        a11 = "Target completion date:"
        a12 = "Date of completion:"
       
   
        if(self.record.issue_solved == "no"):
            the_issue_status = "The issue is open"      
        elif(self.record.issue_solved == "yes"):
            the_issue_status = "The issue is closed"
        else:
            the_issue_status = "No status provided"


        names_list = [str(name) for name in self.record.the_subject_responsible.all()]
        person_responsible = ', '.join(names_list)

        area_list = [str(name) for name in self.record.area.all()]
        site_name = ', '.join(area_list)


        production_issue_list = [str(name) for name in self.record.production_issue.all()]
        production_issue_name = "Production: " + '[' + ', '.join(production_issue_list) + ']'
	
        supplier_issue_list = [str(name) for name in self.record.supplier_issue.all()]
        supplier_issue_name = "Supplier: " + '[' + ', '.join(supplier_issue_list) + ']'

        customer_issues_list = [str(name) for name in self.record.customer_issues.all()]
        the_customer_issues = "Customer: " + '[' + ', '.join(customer_issues_list) + ']'

        other_issues_list = [str(name) for name in self.record.other_issues.all()]
        the_other_issues = "Other: " + '[' + ', '.join(other_issues_list) + ']'

        the_issues = []

        if (production_issue_list): #if the list is not empty - examines boolean value of list
            the_issues.append(production_issue_name)
        if (supplier_issue_list):
            the_issues.append(supplier_issue_name)
        if (customer_issues_list):
            the_issues.append(the_customer_issues)     
        if (other_issues_list):
             the_issues.append(the_other_issues)

        the_severity = ""

        if(self.record.severity == 1):
            the_severity = "Low"
        elif(self.record.severity == 2):
            the_severity = "Medium"
        elif(self.record.severity == 3):
            the_severity = "High"

        area_of_subject =""
        subject_information=""
        subject_areas = []
        information_of_subjects = []

        if(person_responsible): 
            for the_name in names_list:
                p = PersonResponsible.objects.get(title=the_name)

                data_in_supplier = [str(info) for info in p.supplier_set.all()] 

                if(data_in_supplier): 
                    area_of_subject = "Supplier"         
                    subject_areas.append(area_of_subject)
                    subject_information = ''.join(data_in_supplier)
                    information_of_subjects.append(subject_information)

                data_in_delivery_partner = [str(info) for info in p.deliverypartner_set.all()]
                
                if(data_in_delivery_partner):
                    area_of_subject = "Delivery Partner"
                    subject_areas.append(area_of_subject)
                    subject_information = ''.join(data_in_delivery_partner)
                    information_of_subjects.append(subject_information)

                data_in_customer = [str(info) for info in p.customer_set.all()] 
                
                if(data_in_customer): 
                    area_of_subject = "Customer"
                    subject_areas.append(area_of_subject)
                    subject_information = ''.join(data_in_customer)
                    information_of_subjects.append(subject_information)

                data_in_production_company = [str(info) for info in p.productioncompany_set.all()] 
                
                if(data_in_production_company): 
                    area_of_subject = "Production"
                    subject_areas.append(area_of_subject)
                    subject_information = ''.join(data_in_production_company)
                    information_of_subjects.append(subject_information)

                data_in_other_company = [str(info) for info in p.othercompany_set.all()] 
                
                if(data_in_other_company): 
                    area_of_subject = "Other"
                    subject_areas.append(area_of_subject)
                    subject_information = ''.join(data_in_other_company)
                    information_of_subjects.append(subject_information)

                data_in_employee = [str(info) for info in p.employee_set.all()] 
                
                if(data_in_employee): 
                    area_of_subject = "Employee"
                    subject_areas.append(area_of_subject)
                    subject_information = "Internal Employee"
                    information_of_subjects.append(subject_information)


        '''answer fields'''
        b1 = str(self.record.ncr_number)
        b2 = the_issue_datetime
        b3 = self.record.advice_number
        b4 = the_issue_status
        b5 = site_name 
        b6 = ', '.join(the_issues)
        b7 = the_severity
        b8 = person_responsible
        b9 = ', '.join(subject_areas)
        b10 = ', '.join(information_of_subjects)
        b11 = the_target_completion_date 
        b12 = the_closure_date
      

        # tuples containing the data for the text objects
        headings = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12)
        answers = (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12)
        
        # summary title
        textobject = self.c.beginText() 
        textobject.setLeading(30)
        textobject.setFont("Helvetica-Bold", 14)
        textobject.setTextOrigin(inch, inch*5+0.5*cm)
        textobject.textLine("Report Conditions:")
        self.c.drawText(textobject)

        # heading fields output
        lineSpacing=18
        textobject = self.c.beginText()
        textobject.setTextOrigin(inch, inch*5+0.5*cm)
        textobject.moveCursor(0,1.2*cm)  
        textobject.setFont("Helvetica", 10)
        for line in headings:
            textobject.setLeading(lineSpacing)
            textobject.textLine(line) #add the data from the list to the buffer

        self.c.drawText(textobject)
        
        # answer fields output
        textobject = self.c.beginText()
        textobject.setTextOrigin(inch * 4, inch*5+0.5*cm)
        textobject.moveCursor(0,1.2*cm)
        for line in answers:
            textobject.setLeading(lineSpacing)
            textobject.textLine(line)

        self.c.drawText(textobject)
        self.includeFooter(pagenumber)
 

    def page_two(self, pagenumber):           
        self.c.showPage()
        self.c.saveState()
        self.c.setFont('Times-Roman',16)
        self.c.drawString(self.width/2 - 3.5*inch, self.height/2 - 5*inch, "Description")
        self.c.setLineWidth(0.5) 
      
        self.c.bottomup = 1
        self.c.scale(1,-1)
        framedata = []
        frame = Frame(1.6*cm, -10*inch, 7*inch, 9*inch, leftPadding=4*mm, topPadding=6*mm, showBoundary=1)

        '''the paragraph flowable uses XML markup so <br/> creates a new line'''
        root_cause_description = "<b>Root cause of the issue: </b><br/><br/>" + self.record.root_cause + "<br/><br/><br/>"
        basic_description = "<b>Description of the issue: </b><br/><br/>" + self.record.description + "<br/><br/><br/>"

        issue_description = ""
        if(self.record.root_cause):
            issue_description += root_cause_description
        else:
            pass

        if(self.record.description):
            issue_description += basic_description
        else:
            pass

        textstyle = self.styles['Normal']   
        p = Paragraph(issue_description, textstyle)
        framedText = KeepInFrame(maxWidth=0, maxHeight=9*inch, content=[p], mode='shrink')   
        framedata.append(framedText)
        frame.addFromList(framedata, self.c)
        self.c.bottomup = 0
        self.c.restoreState()
        self.includeFooter(pagenumber)

    
    def page_three(self, pagenumber):       
        self.c.showPage()
        self.c.saveState()
        self.c.setFont('Times-Roman',16)
        self.c.drawString(self.width/2 - 3.5*inch, self.height/2 - 5*inch, "Related media")
        self.c.setLineWidth(0.1) 

        try:
            self.c.bottomup = 1
            self.c.scale(1,-1)
            frame = Frame(1.6*cm, -10*inch, 7*inch, 9*inch, leftPadding=4*mm, topPadding=4*mm, showBoundary=1)
            framedata = []                    
            image_list = [str(path) for path in self.record.image_set.all()]
            images_uploaded = len(image_list)
            spacing = Spacer(0,30)
            framedImage = None

            if(images_uploaded == 1):
                var1 = str(os.path.join(settings.BASE_DIR) + str(image_list[0])).replace('\\','/') #make the URL for the image
                framedImage = KeepInFrame(maxWidth=9*inch, maxHeight=9*inch, content=[Image(var1)], hAlign='LEFT', mode='shrink', fakeWidth=False) 
                framedata.append(framedImage)
                frame.addFromList(framedata, self.c)
            elif(images_uploaded == 2):     
                var1 = str(os.path.join(settings.BASE_DIR) + str(image_list[0])).replace('\\','/')
                var2 = str(os.path.join(settings.BASE_DIR) + str(image_list[1])).replace('\\','/')
                framedImage = KeepInFrame(maxWidth=9*inch, maxHeight=9*inch, content=[Image(var1),spacing,Image(var2)], hAlign='LEFT', mode='shrink', fakeWidth=False) 
                framedata.append(framedImage)
                frame.addFromList(framedata, self.c)
            elif(images_uploaded >= 3):     
                var1 = str(os.path.join(settings.BASE_DIR) + str(image_list[0])).replace('\\','/')
                var2 = str(os.path.join(settings.BASE_DIR) + str(image_list[1])).replace('\\','/')
                var3 = str(os.path.join(settings.BASE_DIR) + str(image_list[2])).replace('\\','/')
                framedImage = KeepInFrame(maxWidth=9*inch, maxHeight=9*inch, content=[Image(var1),spacing,Image(var2),spacing,Image(var3)], hAlign='LEFT', mode='shrink', fakeWidth=False)
                framedata.append(framedImage)
                frame.addFromList(framedata, self.c)           
            else:
                textstyle = self.styles['Normal']
                p = Paragraph("Empty", textstyle)
                framedata.append(p)
                frame.addFromList(framedata, self.c)
        except IOError:
            frame = Frame(1.6*cm, -10*inch, 7*inch, 9*inch, leftPadding=4*mm, topPadding=4*mm, showBoundary=1)
            framedata = []      
            p = Paragraph("A problem was encountered when trying to open the uploaded image", None)
            framedata.append(p)
            frame.addFromList(framedata, self.c)
            pass

        self.c.bottomup = 0
        self.c.restoreState()
        self.includeFooter(pagenumber)


    def page_four(self, pagenumber):        
        self.c.showPage()
        self.c.saveState()
        self.c.setFont('Times-Roman',16)
        self.c.drawString(self.width/2 - 3.5*inch, self.height/2 - 5*inch, "Comments")
        self.c.setLineWidth(0.1) 
        text = self.record.comments
       # text += os.path.join(settings.BASE_DIR)
        self.c.bottomup = 1
        self.c.scale(1,-1)
        framedata = []
        frame = Frame(1.6*cm, -10*inch, 7*inch, 9*inch, leftPadding=4*mm, topPadding=4*mm, showBoundary=1)
        textstyle = self.styles['Normal']   
        p = Paragraph(text, textstyle)
        framedText = KeepInFrame(maxWidth=0, maxHeight=9*inch, content=[p], mode='shrink')   
        framedata.append(framedText)
        frame.addFromList(framedata, self.c)
        self.c.bottomup = 0
        self.c.restoreState()
        self.includeFooter(pagenumber)
