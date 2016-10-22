$(document).ready(function() {
  $('#login-button').click(function (e) {
    console.log('ola!');
    e.preventDefault();
    showPlans();
  });
});

var authenticate = function () {
  return {
    name: 'Steve'
  }
};

var showPlans = function () {
  var user = authenticate();
  $.cookie("user", JSON.stringify(user));
  window.location.href = "plans.html";
};
