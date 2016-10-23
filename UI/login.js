var formData = new FormData();
var _ENDPOINT = "http://ec2-54-167-222-78.compute-1.amazonaws.com:27021/"
$(document).ready(function() {
   //Initialize userData object-
   userData = {};
   userData["journeys"] =[];
   $("#btnSubmitDebt").click(function(){
     console.log(this);
     xx=this;
     userData["journeys"].push("Get out of Debt");
     this.setAttribute("class", "btn btn-success");
   });
   $("#btnSubmitRRSP").click(function(){
     userData["journeys"].push("Start an RRSP");
     this.setAttribute("class", "btn btn-success");
   });
   $("#btnSubmitSavings").click(function(){
     userData["journeys"].push("Start a Savings Account");
     this.setAttribute("class", "btn btn-success");
   });


    $("#btnSubmit").click(function(){
      //first join button with username and email - parses field data into userData object
          var x = $("form").serializeArray();
          console.log(x);
          $.each(x, function(i, field){
             console.log(field);
             console.log(field.name);
             userData[field.name] = field.value;
           });
      });
    $("#loginModalSubmit").click(function(){
       //second submit button from modal - again parses form data into userData object
          console.log("in mod submit");
          var x = $("form").serializeArray();
          console.log(x);
          $.each(x, function(i, field){
             console.log(field);
             console.log(field.name);
             console.log(field.vale);
             console.log()
             userData[field.name] = field.value.replace(/\./gi, '');
           });
           //submit to endpoint
           var username = userData.email;
           $.post( [_ENDPOINT+"new_user"].join(), JSON.stringify(userData))
             .done(function( data ) {
               $.get([_ENDPOINT+"user_journey/"].join() + username).then(function (data) {
                 //$.cookie("data", JSON.stringify(data));
                 $.cookie("data", data);
                 window.location.href = "plans.html";
               });
             });
      });

});
