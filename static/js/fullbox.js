document.addEventListener('DOMContentLoaded', function() {
    set_bloclk_height();
});


$(window).on('resize', function() {
	set_bloclk_height();
});


function set_bloclk_height() {
    get(".fullbox").style.height = window.innerHeight + 'px';
}