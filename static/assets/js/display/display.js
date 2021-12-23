
var months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
var myDays = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu"];
var date = new Date();
var day = date.getDate();
var month = date.getMonth();
var thisDay = date.getDay(),
    thisDay = myDays[thisDay];
var yy = date.getYear();
var year = (yy < 1000) ? yy + 1900 : yy;

// -----------------------------------------------------
function startTime() {
    var today = new Date(),
        curr_hour = today.getHours(),
        curr_min = today.getMinutes(),
        curr_sec = today.getSeconds();
    curr_hour = checkTime(curr_hour);
    curr_min = checkTime(curr_min);
    curr_sec = checkTime(curr_sec);
    document.getElementById('clock').innerHTML = thisDay + ', ' + day + ' ' + months[month] + ' ' + year + ' | ' + curr_hour + ":" + curr_min + ":" + curr_sec;
}

function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

setInterval(startTime, 500);


var i = 0;
var mapsHtml = '';
$.ajax({
    url: '{{URL::to('get-maps')}}',
    type: 'GET',
    success: function (data) {
        for (i = 0; i < data[0].length; i++) {
            mapsHtml += '<li class="li-animate-maps" id="a1">' +
                '        <table class="table card-table">' +
                '            <tbody>' +
                '            <tr style=" border-bottom: 1px solid gray; height: 50%; border-bottom: 1px solid #E0E5EC;">' +
                '                <td style="width:1%; line-height: normal">' + (i+1) + '</td>' +
                '                <td style="width:19%; text-align: left; line-height: normal">' + data[0][i].tgl_agenda + '</td>' +
                '                <td style="width:80%; text-align: left; line-height: normal">' + data[0][i].judul_agenda + '</td>' +
                '            </tr>' +
                '            </tbody>' +
                '        </table>' +
                '    </li>'
        }
        $('.ul-animate-maps').html(mapsHtml);
        $('#number').text(data[1]);
        $('#number1').text(data[2]);
    }
});

var steps = 1;

$(function maps() {
    var top = '-=' + (steps * $('.li-animate-maps').height()) + 'px';
    var lis = $('.li-animate-maps:lt(' + steps + ')');
    var clones = $(lis).clone();
    clones.appendTo('.ul-animate-maps');
    $.when(
        $('.li-animate-maps').animate({top: top}, 'slow')
    ).done(function () {
        clones.remove();
        lis.appendTo('.ul-animate-maps');
        $('.li-animate-maps').css('top', 'auto');
        setTimeout(maps, 5000);
    });
});

var steps = 1;
$(function dpis() {
    var top = '-=' + (steps * $('.li-animate-dpis').height()) + 'px';
    var lis = $('.li-animate-dpis:lt(' + steps + ')');
    var clones = $(lis).clone();
    clones.appendTo('.ul-animate-dpis');
    $.when(
        $('.li-animate-dpis').animate({top: top}, 'slow')
    ).done(function () {
        clones.remove();
        lis.appendTo('.ul-animate-dpis');
        $('.li-animate-dpis').css('top', 'auto');
        setTimeout(dpis, 5000);
    });
});

var steps = 1;
$(function gsmh() {
    var top = '-=' + (steps * $('.li-animate-gsmh').height()) + 'px';
    var lis = $('.li-animate-gsmh:lt(' + steps + ')');
    var clones = $(lis).clone();
    clones.appendTo('.ul-animate-gsmh');
    $.when(
        $('.li-animate-gsmh').animate({top: top}, 'slow')
    ).done(function () {
        clones.remove();
        lis.appendTo('.ul-animate-gsmh');
        $('.li-animate-gsmh').css('top', 'auto');
        setTimeout(gsmh, 5000);
    });
});

// $(function () {
//     $('#number').each(function () {
//         $(this).prop('Counter', 0).animate({
//             Counter: $(this).text()
//         }, {
//             duration: 5000,
//             easing: 'swing',
//             step: function (now) {
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
//
//     $('#number1').each(function () {
//         $(this).prop('Counter', 0).animate({
//             Counter: $(this).text()
//         }, {
//             duration: 5000,
//             easing: 'swing',
//             step: function (now) {
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
//     $('#number2').each(function () {
//         $(this).prop('Counter', 0).animate({
//             Counter: $(this).text()
//         }, {
//             duration: 5000,
//             easing: 'swing',
//             step: function (now) {
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
//     $('#number3').each(function () {
//         $(this).prop('Counter', 0).animate({
//             Counter: $(this).text()
//         }, {
//             duration: 5000,
//             easing: 'swing',
//             step: function (now) {
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
//     $('#number4').each(function () {
//         $(this).prop('Counter', 0).animate({
//             Counter: $(this).text()
//         }, {
//             duration: 5000,
//             easing: 'swing',
//             step: function (now) {
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
//     $('#number5').each(function () {
//         $(this).prop('Counter', 0).animate({
//             Counter: $(this).text()
//         }, {
//             duration: 5000,
//             easing: 'swing',
//             step: function (now) {
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
//     $('#number6').each(function () {
//         $(this).prop('Counter', 0).animate({
//             Counter: $(this).text()
//         }, {
//             duration: 5000,
//             easing: 'swing',
//             step: function (now) {
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
//     $('#number7').each(function () {
//         $(this).prop('Counter', 0).animate({
//             Counter: $(this).text()
//         }, {
//             duration: 5000,
//             easing: 'swing',
//             step: function (now) {
//                 $(this).text(Math.ceil(now));
//             }
//         });
//     });
//
// });