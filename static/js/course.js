document.addEventListener('DOMContentLoaded', function() {
    set_height();
});


$(window).on('resize', function() {
	set_height();
});


function set_height() {
    let window_width = window.innerWidth;
    let window_height = window.innerheight;
    let body_height = get("body").offsetHeight;
	let header_height = get("header").offsetHeight;

    if (window_width > 768) {
        let main_height = body_height - header_height;
        get("main").style.height = main_height + 'px';
        get(".map").style.height = get(".main-block").clientHeight + 'px';
    } else {
        let main_height = 'auto';
        get("main").style.height = main_height;
        get(".map").style.height = 50 + 'vh';
    }
}