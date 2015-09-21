
$(document).ready(function () {


    $("#submitsingin").click(function(){

        var u = $("#username").val();
        var p = $("#password").val();
                console.log(u);
        console.log(p);
        var csrftoken = getCookie('csrftoken');
        console.log(csrftoken);
        $("#msg").html('<div class="alert alert-info" role="alert">Singing in, please wait a while!!! </b><img src="/static/images/load.GIF" /></div>');
        $.ajax({
            type: "post",
            async: true,
            cache: false,

            url: "account/signin/",
            data: { csrfmiddlewaretoken: csrftoken, username: u, password: p  },
            success: function(msg){
                $(location).attr('href', '/competitions');
            },
            error: function(data){
                console.log(data);
                $("#msg").html('<div class="alert alert-warning alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Error!</strong> Username or password are wrong, please try again!!!.</div>');
            }
        });
    });


    $("#submitsignup").click(function(){

        if ( $("#passwordSU").val() !== '') {
            alert ('Password field is empty');
            return false;
        }

        if ( $("#confirmpasswordSU").val() !== '') {
            alert ('Confirm password field is empty');
            return false;
        }

        if ( $("#passwordSU").val() !== $("#confirmpasswordSU").val()) {
            alert ('Password fields have not the same value');
            return false;
        }

        var u = $("#usernameSU").val();
        var p = $("#passwordSU").val();
        var cn = $("#companynameSU").val();
        var e = $("#emailSU").val();

        var csrftoken = getCookie('csrftoken');

        $("#msgSU").html('<div class="alert alert-info" role="alert">Singing Up, please wait a while!!! </b><img src="/static/images/load.GIF" /></div>');

        $.ajax({
            type: "post",
            async: true,
            cache: false,

            url: "account/signup/",
            data: { csrfmiddlewaretoken: csrftoken, username: u, password: p, email:e, companyname:cn },
            success: function(msg){
                console.log(msg);

                if (msg.msg =="OK"){
                    $(location).attr('href', '/competitions');
                }

                if (msg.msg =="USEREXIST"){
                    $("#msgSU").html('<div class="alert alert-warning alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Error!</strong> The user already exist!!!.</div>');
                }
            },
            error: function(data){
               $("#msgSU").html('<div class="alert alert-warning alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button><strong>Error!</strong> Something went wrong, please try again!!!.</div>');
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
