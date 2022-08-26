function create_progressbar(id) {
    get(id).innerHTML += `
        <div class="progressbar-part done"></div>
        <div class="progressbar-part locked-part"></div>
        <div class="progressbar-part locked-part"></div>
        <div class="progressbar-part locked-part"></div>
        <div class="progressbar-part locked-part"></div>
        <div class="progressbar-part locked-part"></div>
    `
}