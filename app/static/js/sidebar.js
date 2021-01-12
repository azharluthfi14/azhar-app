$(document).ready(function () {
    $('.sideMenuToggler').on('click', function () {
        $('.wrapper').toggleClass('active');
    });

    // var adjustSidebar = function () {
    //     $('.sidebar').slimScroll({
    //         height: document.documentElement.clientHeight - $('.navbar').outerHeight(),
    //         zIndex: 90
    //     });
    // };

    // adjustSidebar();
    // $(window).resize(function () {
    //     adjustSidebar();
    // });


});