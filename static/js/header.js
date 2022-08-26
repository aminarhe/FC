var isOpen = false;

function dropdown_menu() {
    let dropdown = get(".dropdown");
    
    if (!isOpen) {
        dropdown.style.display = 'flex';
        isOpen = true;
    } else {
        dropdown.style.display = 'none';
        isOpen = false;
    }
}