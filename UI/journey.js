$(document).ready(function() {
  var data = JSON.parse($.cookie("data"));
  var index = $.cookie("journey-index");
  var journey = data.journeys[index];

  $('#logout-button').click(function (e) {
    e.preventDefault();
    window.location.href = "/UI/";
  });
});
