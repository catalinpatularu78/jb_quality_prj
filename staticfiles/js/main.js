/*!
* Start Bootstrap - Bare v5.0.7 (https://startbootstrap.com/template/bare)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


// function to convert DD:HH:MM to minutes 



function add_number() {
    let text1 = document.getElementById("Text1");
    let text2 = document.getElementById("Text2");
    let text3 = document.getElementById("Text3");

    let first_number = parseInt(text1.value);
    if (isNaN(first_number)) first_number = 0;
    let second_number = parseInt(text2.value);
    if (isNaN(second_number)) second_number = 0;
    let third_number = parseInt(text3.value);
    if (isNaN(third_number)) third_number = 0;
    var result = (first_number * 1440)  + (second_number * 60 ) + third_number;


    document.getElementById("id_downtime_time").value = result;
}


