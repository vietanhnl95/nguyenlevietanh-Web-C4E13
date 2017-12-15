/** smooth scroll function */
var main = function() {
  $(document).on('click', 'a[href^="#cafe-list"]', function (event) {
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
});
}

$(document).ready(main);
