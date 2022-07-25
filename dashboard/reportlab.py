import io, os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm, cm
from reportlab.lib.pagesizes import A4
#from .models import Post
from django.conf import settings
from django.http import HttpResponse
from reportlab.platypus import Paragraph, Image, Frame, KeepInFrame
from reportlab.lib.colors import *
from reportlab.lib.enums import *


class Report:

    report_title = "NCR report.pdf"

    def __init__(self, filename):   

        self.filename = filename        
        self.pagesize = A4
        self.width, self.height = self.pagesize
        self.buffer = io.BytesIO()
        self.styles = getSampleStyleSheet()
        self.c = self.createCanvas(self.buffer)
  

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

    
    def generate(request):
        doc = Report(Report.report_title)
        response = HttpResponse()
        response.content = doc.getBuffer()
        response.headers['Content-Disposition'] = 'inline; filename=' + doc.filename
        response.headers['Content-Type'] = 'application/pdf'
        
        return response


    def includeFooter(self, pageNumber):                
        footer_line_h = self.height-60   
        self.c.line(cm, footer_line_h, self.width - inch + 1.05*cm, footer_line_h) 
        self.c.setFont("Times-Roman", 8)    
        self.c.drawString(1.1*cm, footer_line_h+10, "Report:")
        self.c.drawString(inch, footer_line_h+10, "NCR Report")
        self.c.drawString(4.5*inch+cm, footer_line_h+10, "https://github.com/Sphaze/")
        self.c.drawString(7*inch+7*mm, footer_line_h+10, "Page %d" % pageNumber)



    def page_one(self, pagenumber):   
        logo = os.path.join(settings.STATIC_ROOT,"img/jandb_logo.jpg")       
        logoX = (self.width/2) + 2*inch - 1*mm
        logoY = 3.38 * inch
        logoSize = 120
        self.c.saveState()
        self.c.scale(1,-1)
        self.c.drawInlineImage(logo, width=logoSize, x=logoX, y=-logoY, preserveAspectRatio=True)
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
        textobject.textLine("Comment:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+2*cm+2*mm)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+3*cm)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Created by:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+3.5*cm+2*mm)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)

        
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
        textobject.textLine("placeholder")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+1.5*cm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Execution time:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+2*cm+2*mm)
        textobject.moveCursor(3*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)


        ### right column ###
        
        ''' heading blob '''  
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Current Date:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+0.5*cm+2*mm)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("20/07/2022")
        self.c.drawText(textobject)
        ''' heading blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+1.5*cm)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(heading_font, heading_fontsize)
        textobject.textLine("Job ID:")
        self.c.drawText(textobject)
        ''' answer blob '''
        textobject = self.c.beginText()
        textobject.setTextOrigin(1.3*cm, 2*inch+2*cm+2*mm)
        textobject.moveCursor(6*inch,0)
        textobject.setFont(answer_font, answer_fontsize)
        textobject.textLine("placeholder")
        self.c.drawText(textobject)

        #data = Post.objects.last() #most recent database object from my database model called "Post"
        
        '''headings'''

        a1 = "NCR ID:"
        a2 = "Date of NCR:"
        a3 = "Advice Number:"
        a4 = "Job Reference Number:"
        a5 = "Status:"
        a6 = "Non Conformance Code:"
        a7 = "Company:"
        a8 = "Site:"
        a9 = "Severity:"
        a10 = "Person responsible:"
        a11 = "NCR Status:"
        a12 = "Target completion date:"
        a13 = "Date of completion:"

        '''convert ISO timestring (2022-07-13 11:53:52+00:00) to date with desired format '''

       # NCR_date = str(str(data.date_posted)[8:10]) +'/'+str(str(data.date_posted)[5:7])+'/'+str(str(data.date_posted)[0:4])
    
        '''answers'''

        b1 = "A20109" #str(data.ncr_number)
        b2 = "13/07/2022" # NCR_date
        b3 = "This is test text"
        b4 = "This is test text"
        b5 = "This is test text"
        b6 = "This is test text"
        b7 = "This is test text"
        b8 = "This is test text"
        b9 = "This is test text"
        b10 = "This is test text"
        b11 = "This is test text"
        b12 = "This is test text"
        b13 = "This is test text"
     

        # tuples containing the data for the text objects
        headings = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)
        answers = (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13)
        
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
        self.c.setLineWidth(0.1) 
        text = '''It is a paradisematic country, in which roasted parts of
                sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts.It is a
                paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing
                has no control about the blind texts. It is a paradisematic country, in which roasted parts of
                sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts.It is a
                paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing
                has no control about the blind texts.'''     
        self.c.bottomup = 1
        self.c.scale(1,-1)
        framedata = []
        frame = Frame(1.6*cm, -10*inch, 7*inch, 9*inch, leftPadding=3*mm, showBoundary=1)
        textstyle = self.styles['Normal']   
        p = Paragraph(text, textstyle)
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
        media = Image(os.path.join(settings.STATIC_ROOT,"img/eng_building.jpg"), useDPI=True)
        self.c.bottomup = 1
        self.c.scale(1,-1)
        framedata = []
        frame = Frame(1.6*cm, -10*inch, 7*inch, 9*inch, leftPadding=4*mm, topPadding=4*mm, showBoundary=1)
        framedImage = KeepInFrame(maxWidth=5*inch, maxHeight=6*inch, content=[media], hAlign='LEFT', mode='shrink', fakeWidth=False) 
        framedata.append(framedImage)
        frame.addFromList(framedata, self.c)
        self.c.bottomup = 0
        self.c.restoreState()
        self.includeFooter(pagenumber)


    def page_four(self, pagenumber):        
        self.c.showPage()
        self.c.saveState()
        self.c.setFont('Times-Roman',16)
        self.c.drawString(self.width/2 - 3.5*inch, self.height/2 - 5*inch, "Comments")
        self.c.setLineWidth(0.1) 
        text = "Far far away, behind the word mountains.... "
        self.c.bottomup = 1
        self.c.scale(1,-1)
        framedata = []
        frame = Frame(1.6*cm, -10*inch, 7*inch, 9*inch, leftPadding=3*mm, showBoundary=1)
        textstyle = self.styles['Normal']   
        p = Paragraph(text, textstyle)
        framedText = KeepInFrame(maxWidth=0, maxHeight=9*inch, content=[p], mode='shrink')   
        framedata.append(framedText)
        frame.addFromList(framedata, self.c)
        self.c.bottomup = 0
        self.c.restoreState()
        self.includeFooter(pagenumber)

    
