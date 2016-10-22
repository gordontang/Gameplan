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
  var data = authenticate();
  $.cookie("data", JSON.stringify(data));
  window.location.href = "plans.html";
};

var authenticate = function () {
  return {
   "user":"steve",
   "bankaccount":false,
   "rrsp":true,
   "age":"30-40",
   "income":"40k-50k",
   "kids":true,
   "journeys":[
      {
         "journey":"Start an RRSP",
         "steps":[
            {
               "type":"learning",
               "description":"Learn about Banking Services",
               "link":"http://prospercanada.org/prospercanada/media/PDF/Facilitator%20Tools/English/Module%204/Participant_Handbook_Module-4.pdf",
               "points":"10",
               "complete":"false"
            },
            {
               "type":"behavioral",
               "description":"Talk to a financial advisor at your bank",
               "link":"",
               "points":"5",
               "complete":"false"
            },
            {
               "type":"learning",
               "description":"learn about savings",
               "link":"http://prospercanada.org/prospercanada/media/PDF/Facilitator%20Tools/English/Module%205/Participant_Handbook_Module-5.pdf",
               "points":"5",
               "complete":"false"
            },
            {
               "type":"behavioral",
               "description":"Open an RRSP",
               "link":"",
               "points":"10",
               "complete":"false"
            },
            {
               "type":"behavioral",
               "description":"Setup Auto deposit",
               "link":"",
               "points":"25",
               "complete":"false"
            }
         ]
      },
      {
         "journey":"Start a Savings Account",
         "steps":[
            {
               "type":"learning",
               "description":"Learn about Banking Services",
               "link":"http://prospercanada.org/prospercanada/media/PDF/Facilitator%20Tools/English/Module%204/Participant_Handbook_Module-4.pdf",
               "points":"10",
               "complete":"false"
            },
            {
               "type":"behavioral",
               "description":"Visit bank and open a savings account",
               "link":"",
               "points":"5",
               "complete":"false"
            },
            {
               "type":"learning",
               "description":"learn about savings",
               "link":"http://prospercanada.org/prospercanada/media/PDF/Facilitator%20Tools/English/Module%205/Participant_Handbook_Module-5.pdf",
               "points":"5",
               "complete":"false"
            },
            {
               "type":"behavioral",
               "description":"Depost $50 in account",
               "link":"",
               "points":"10",
               "complete":"false"
            },
            {
               "type":"behavioral",
               "description":"Setup Auto deposit",
               "link":"",
               "points":"25",
               "complete":"false"
            }
         ]
      }
   ]
}
};
