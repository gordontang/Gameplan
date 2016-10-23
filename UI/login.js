var formData = new FormData();

$(document).ready(function() {
   //Initialize userData object-
   userData = {};
   userData["journeys"] =[];
   $("#btnSubmitDebt").click(function(){
     console.log(this);
     xx=this;
     userData["journeys"].push("Get out of Debt");
     this.setAttribute("class", "btn btn-success");
     this.textContent('Added');
   });
   $("#btnSubmitRRSP").click(function(){
     userData["journeys"].push("Start an RRSP");
     this.setAttribute("class", "btn btn-success");
     this.textContent('Added');
   });
   $("#btnSubmitSavings").click(function(){
     userData["journeys"].push("Start a Savings Account");
     this.setAttribute("class", "btn btn-success");
     this.textContent('Added');
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
           $.post( "http://ec2-54-167-222-78.compute-1.amazonaws.com:27021/new_user", JSON.stringify(userData))
             .done(function( data ) {
              //send to landing
             });
      });

});
