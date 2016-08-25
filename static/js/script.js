$(document).ready(function (){
  var btn = $("#formbtn");
  btn.click(function(){
    console.log('123');
    var username = $('#username').val();
    var password = $('#password').val();
    $.post('/', {
      username: username,
      password: password
    });
  });
});
