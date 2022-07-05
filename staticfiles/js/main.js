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

