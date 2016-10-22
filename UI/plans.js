$(document).ready(function() {
  displayUserInfo();
  captureDates();

  $('#logout-button').click(function (e) {
    e.preventDefault();
    window.location.href = "/";
  });
});

var displayUserInfo = function () {
  var user = JSON.parse($.cookie("user"));
  $('#username')[0].innerHTML = 'Welcome ' + user.name + '!';
};

var captureDates = function () {
  var date = new Date();
  $('#plan-current-date')[0].innerHTML = monthNames[date.getMonth()] + ' ' + date.getDate();

  var endOfYear = new Date(new Date().getFullYear(), 11, 31);
  var diffDays = Math.round(Math.abs((date.getTime() - endOfYear.getTime())/(24*60*60*1000))) + 1;
  $('#plan-til-end')[0].innerHTML = diffDays + ' left in ' + date.getFullYear();
};

var monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];
