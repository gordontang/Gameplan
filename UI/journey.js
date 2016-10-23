$(document).ready(function() {
  var data = JSON.parse($.cookie("data"));
  var index = $.cookie("journey-index");
  var journey = data.journey_details[index];

  $('#logout-button').click(function (e) {
    e.preventDefault();
    window.location.href = "/UI/";
  });

  displaySteps(journey);
});

var displaySteps = function (journey) {
  console.log(journey);
  $('#journey-icon').attr('src', getJourneyIcon(journey));
  var node = $('#accomplishments');

  var template = `<div class="row" style="margin-bottom:10px;">
    <div class="col-md-6">
        <p style="font-size:2rem;"><span class="label label-info counter" style="font-size:1.4rem;margin-right: 10px;"></span><span class="text"></span><a class="link"></a></p>
    </div>
    <div class="col-md-1" style="font-size:2.2rem;">
      <input type="checkbox" />
    </div>
  </div>`;

  var i;
  var steps = journey.steps;
  for (i = 0; i < steps.length; i++) {
    var e = $(template);
    $('.counter', e).html(i + 1);
    if (steps[i].link) {
      $('.link', e).attr('href', steps[i].link);
      $('.link', e).html(steps[i].description);
    } else {
      $('.text', e).html(steps[i].description);
    }
    $('input', e).prop('checked', steps[i].complete !== "false");
    node.append(e);
  }
  node.append($('<hr />'));
  node.append($('<p style="font-size:2rem;">' + (steps.length - journey.current_step) + ' MORE TASKS TO GO!</p>'));
};

var getJourneyIcon = function (journey) {
  switch(journey.journey) {
    case 'Start an RRSP':
      return 'static/rrspcourt.png';
    case 'Start a Savings Account':
      return 'static/savings300.png';
    default:
      return 'static/creditcard300.png';
  }
};
