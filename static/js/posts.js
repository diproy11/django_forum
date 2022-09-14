$(function(){
    //Executed when js-menu-icon js clicked
    $('.menu_icon').click(function(){
        //$(this) : Self element,namely div.js-menu-icon
        //next() : Next to div.js-menu-icon,namely div.menu
        //toggle : Switch show and hide
        $(this).next().toggle();
    })
})