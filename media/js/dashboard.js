$(document).ready(function() {
    $(".btn-slide").click(function() {

        $("#panel").slideToggle("slow");
        $(this).toggleClass("active");
        return false;

    });

     //hide message_body after the first one
    $(".message_list .message_body:gt(0)").hide();

        //hide message li after the 5th
    $(".message_list li:gt(4)").hide();


        //toggle message_body
    $(".message_head").click(function() {
        $(this).next(".message_body").slideToggle(500)
        return false;
    });

        //collapse all messages
    $(".collpase_all_message").click(function() {
        $(".message_body").slideUp(500)
        return false;
    });

        //show all messages
    $(".show_all_message").click(function() {
        $(this).hide()
        $(".show_recent_only").show()
        $(".message_list li:gt(4)").slideDown()
        return false;
    });

        //show recent messages only
    $(".show_recent_only").click(function() {
        $(this).hide()
        $(".show_all_message").show()
        $(".message_list li:gt(4)").slideUp()
        return false;
    });
});

/*
 * Banner Slider
 *
 * Copyright © 2009 Leonard Chan
 * All rights reserved.
*/

var theInt = null;
var $crosslink, $navthumb;
var curclicked = 0;

theInterval = function(cur) {
    clearInterval(theInt);

    if (typeof cur != 'undefined')
        curclicked = cur;

    $crosslink.removeClass("active-thumb");
    $navthumb.eq(curclicked).addClass("active-thumb");
    $(".stripNav ul li a").eq(curclicked).trigger('click');

    theInt = setInterval(function() {
        $crosslink.removeClass("active-thumb");
        $navthumb.eq(curclicked).addClass("active-thumb");
        $(".stripNav ul li a").eq(curclicked).trigger('click');
        curclicked++;
        if (6 == curclicked)
            curclicked = 0;

    }, 6000);
};

$(function() {

    $("#main-photo-slider").codaSlider();

    $navthumb = $(".cross-link");
    $crosslink = $(".cross-link");

    $navthumb.click(function() {
        var $this = $(this);
        theInterval($this.attr('href').slice(1) - 1);
        return false;
    });

    theInterval();
});

/*
 * Accordian Effects
 *
 * Copyright © 2009 Leonard Chan
 * All rights reserved.
*/

jQuery().ready(function() {

    // second simple accordion with special markup
    jQuery('#accordion').accordion({
        navigation: true,
        event: 'mouseover',
        animated: 'bounceslide',
        autoHeight: false
    });

});
	
		