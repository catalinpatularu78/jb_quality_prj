/*!
* Start Bootstrap - Bare v5.0.7 (https://startbootstrap.com/template/bare)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


// function to convert DD:HH:MM to minutes 






function add_number() {

    const day_number = parseInt((document.getElementById("DayConversion").value)* 1440 || 0) ;  // 0 or get day value multiplied by minutes per day 
    const hour_number = parseInt(document.getElementById("HourConversion").value * 60 || 0);    // 0 or get hour value multiplied by minutes per hour
    const minute_number = parseInt(document.getElementById("MinuteConversion").value) || 0;     // 0 or get minutes value

    document.getElementById("id_downtime_time").value = day_number + hour_number + minute_number; // total value -> html element 
}


function add_number_comp_time() {

    const EstCompday_number = parseInt((document.getElementById("EstCompDayConversion").value)* 1440 || 0) ;  // 0 or get day value multiplied by minutes per day 
    const EstComphour_number = parseInt(document.getElementById("EstCompHourConversion").value * 60 || 0);    // 0 or get hour value multiplied by minutes per hour
    const EstCompminute_number = parseInt(document.getElementById("EstCompMinuteConversion").value) || 0;     // 0 or get minutes value

    document.getElementById("id_estimated_completion_time").value = EstCompday_number + EstComphour_number + EstCompminute_number; // total value -> html element 
}




function show_issue_affect_element() {

    const conditional_element_select = document.getElementById("id_issue_affect_other_areas").value;
    const hidden_element  = document.getElementById("issue_affect_other_areas_card"); 
    
    if (conditional_element_select  === 'yes') {
        hidden_element.classList.toggle('d-none');
        }else {
            hidden_element.classList.add('d-none');
        }
}







if (document.querySelector('#client-search') !== null) {

    document.querySelector('#client-search').addEventListener('input' , filterList);

    function filterList(){
        const searchInputClient = document.querySelector('#client-search');
        const filterClient = searchInputClient.value.toLowerCase();
        const listItemsClient = document.querySelectorAll('#client_list');
    
        listItemsClient.forEach((item) => {
            let text = item.textContent;
            if(text.toLowerCase().includes(filterClient.toLowerCase())){
                item.style.display = '';
            } else{
                item.style.display = 'none';
            }
            
        });
    }
}


if (document.querySelector('#the_subject_responsible-search') !== null) {

    document.querySelector('#the_subject_responsible-search').addEventListener('input' , the_subject_responsiblefilterList);

    function the_subject_responsiblefilterList(){
        const searchInputResponsible = document.querySelector('#the_subject_responsible-search');
        const filterResponsible = searchInputResponsible.value.toLowerCase();
        const listItemsResponsible = document.querySelectorAll('#subject_responsible_list');

        listItemsResponsible.forEach((item) => {
            let text = item.textContent;
            if(text.toLowerCase().includes(filterResponsible.toLowerCase())){
                item.style.display = '';
            } else{
                item.style.display = 'none';
            }
            
        });
    }
}


$( document ).ready(function ()
{
    //Render Interactive CSS:
    var Link = document.createElement('link'); Link.rel = 'stylesheet';
    Link.href = 'C:\Users\hp\Desktop\Main Project\jb_quality_prj\static\css\style.css';
    var Head = document.getElementsByTagName('head')[0];
    Head.parentNode.insertBefore(Link, Head);
});