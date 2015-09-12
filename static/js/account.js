$(document).ready(function () {

    $("#submitmodal").click(function(){
        var u = $("#username").val();
        var p = $("#password").val();
        var csrftoken = getCookie('csrftoken');
    console.log(csrftoken);
        $.ajax({
            type: "post",
            async: true,
            cache: false,

            url: "account/singin/",
            data: { csrfmiddlewaretoken: csrftoken, username: u, password: p  },
            success: function(msg){
                 //hide button and show thank you
                //$("#form-content").modal('hide'); //hide popup
                $(location).attr('href', '/competition')
            },
            error: function(data){
            console.log(data);
                $("#error").html('<div class="alert alert-danger">Username or password are wrong, please try again!!!</div>');
            }
        });
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
