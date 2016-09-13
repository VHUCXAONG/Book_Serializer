var username, password;

function setCookie(name, value, expire){
  var date = new Date();
  date.setDate(date.getDate() + expire);
  document.cookie = name + "=" + escape(value) + ((expire == null) ? "" : ";expires=" + date.toGMTString());
}

function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i].trim();
    if (c.indexOf(name) == 0)
      return c.substring(name.length,c.length);
  }
  return "";
}

function logSuccess() {
  username = getCookie('username');
  var book_menu = $('#book_menu');
  var change_menu = $('#change_menu');
  console.log(menu);
  $.post('/loadbook',function(data) {
    console.log(data);
    console.log(data.book_name);
    for (var i = 0; i < data.book_name.length; i++) {
      var name = data.book_name[i];
      var new_li = '<li><a>' + name + '</a></li>';
      var new_change = '<li><a href="/add">' + name + '</a></li>';
      book_menu.append(new_li);
      change_menu.append(new_change);
    }
  });
}


$(document).ready(function(){
  var href = location.href;
  url_list = href.split("/");
  current_page = url_list[url_list.length - 1];
  console.log(current_page);
  if (current_page == 'book') {
    logSuccess();
  }
  else {
    if (getCookie('username') != "" && getCookie('password') != "") {
      username = getCookie('username');
      password = getCookie('password');
      $.post('/login', {
        username: username,
        password: password,
        remember_me: true
      }, function(data) {
        if (data.auth){
          window.location.href = '/book';
          logSuccess();
        }
      });
    }
    else{
      var btn = $("#formbtn");
      btn.click(function() {
        username = $('#username').val();
        password = $('#password').val();
        remember_me = $('#remember_me').is(':checked');
        $.post('/login', {
          username: username,
          password: password,
          remember_me: remember_me
        }, function(data) {
          if (data.auth) {
            if (data.isCookie){
                setCookie('username', username, 1);
                setCookie('password', password, 1);
            }
            console.log(document.cookie);
            console.log(getCookie('username'));
            window.location.href = '/book';
            logSuccess();
          }
          else {
            $('#logerror').text('invalid username or password');
          }
        });
      });
    }
  }
});
