$(document).ready(function() {
  $('#login-button').click(function (e) {
    e.preventDefault();
    showPlans();
  });

  $(".dropdown-menu li a").click(function(){
    $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
    $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
  });
});

var showPlans = function () {
  var username = $("input:text[name=email]" ).val();
  //var _ENDPOINT = "http://ec2-54-167-222-78.compute-1.amazonaws.com:27021/user_journey/";
  $.get([_ENDPOINT+"user_journey/"].join() + username).then(function (data) {
    //$.cookie("data", JSON.stringify(data));
    $.cookie("data", data);
    window.location.href = "plans.html";
  });
};
