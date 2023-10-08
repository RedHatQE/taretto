$(document).ready(function () {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 50)  /*height in pixels when the navbar becomes non opaque*/ 
        {
            $('.navbar-opaque').addClass('opaque');
        }
        else {
            $('.navbar-opaque').removeClass('opaque');
        }
    });
});
