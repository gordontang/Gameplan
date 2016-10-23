$(document).ready(function() {
  displayUserInfo();
  captureDates();
  displayJourneys();

  $('#logout-button').click(function (e) {
    e.preventDefault();
    window.location.href = "/UI/";
  });

  $('.journey-button').click(function (e) {
    console.log(e);
    $.cookie("journey-index", e.target.getAttribute('selection'));
    window.location.href = "journey.html";
  });
});

var displayJourneys = function () {
  var user = JSON.parse($.cookie("data"));
  console.log(user);
  var journeys = user.journeys;
  console.log(journeys);
  console.log(journeys.length);
  var i;
  var node = $('#journeys');

  for (i = 0; i < journeys.length; i++) {
    console.log(i);
    var icon = getJourneyIcon(journeys[i]);
    console.log(icon);
    var e = $('<div class="col-md-4 text-center"><img height="300" width="300" /><button type="button" class="btn btn-info journey-button" style="margin-top:10px;">GET MOVING</button></div>');
    $('img', e).attr('src', icon);
    $('button', e).attr('selection', i);
    node.append(e);
  }
};

var getJourneyIcon = function (journey) {
  console.log("looking for icon");
  console.log(journey);
  //not catching
  switch(journey) {
    case 'Start an RRSP':
      return '../assets/rrspcourt.png';
    case 'Start a Savings Account':
      return '../assets/savings300.png';
    default:
      return '../assets/payoffdebt.png';
  }
};

var displayUserInfo = function () {
  var user = JSON.parse($.cookie("data"));
  $('#username')[0].innerHTML = 'Welcome ' + user.email + '!';
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
