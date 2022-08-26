document.addEventListener('DOMContentLoaded', function(){

    $('#code').linenumbers();	

});


function get_code(username) {
    let code = get("#code").value;

    if (code.length > 0) {
    
        $.ajax({
            url: `/compile/${username}`,
            type: 'POST',
            data: {
                code: code,
            },
            dataType : 'json',
            success: function (data) {
                alert(data['result']);
            },
            error: function(jqxhr, status, errorMsg) {
                alert(jqxhr, status, errorMsg);
            }
        });
    
    } else {
        alert('Console is empty!')
    }
}

function clear_console() {
    let isOk = confirm("Are you sure you want to clear the console?");
    if (isOk) {
        get("#code").value = "";
    }
}