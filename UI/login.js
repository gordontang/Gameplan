var formData = new FormData();
$(document).ready(function() {
   //Initialize userData object-
   userData = {};

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
             userData[field.name] = field.value;
           });
           //submit to endpoint
           $.post( "http://ec2-54-167-222-78.compute-1.amazonaws.com:27021/new_user", JSON.stringify(userData))
             .done(function( data ) {
              //send to landing
             });
      });

});
