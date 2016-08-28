function setCookie(name, value, expire){
  var date = new Date();
  date.setDate(date.getDate() + expire);
  document.cookie = name + "=" + escape(value) + ((expire == null) ? "" : ";expires=" + date.toGMTString());
}

function getCookie(cname){
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i].trim();
    if (c.indexOf(name) == 0)
      return c.substring(name.length,c.length);
  }
  return "";
}

$(document).ready(function (){
  var username, password;
  if (getCookie('username') != "" && getCookie('password') != "") {
    username = getCookie('username');
    password = getCookie('password');
    $.post('/login', {
      username: username,
      password: password,
      remember_me: true
    }, function(data){
      if (data.auth){
        window.location.href = "/a123";
      }
    });
  }
  else{
    var btn = $("#formbtn");
    btn.click(function(){
      username = $('#username').val();
      password = $('#password').val();
      remember_me = $('#remember_me').is(':checked');
      $.post('/login', {
        username: username,
        password: password,
        remember_me: remember_me
      }, function(data){
        if (data.auth) {
          if (data.isCookie){
              setCookie('username', username, 1);
              setCookie('password', password, 1);
          }
          console.log(document.cookie);
          console.log(getCookie('username'));
          window.location.href = "/a123";
        }
        else {
          $('#logerror').text('invalid username or password');
        }
      });
    });
  }
});
