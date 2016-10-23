function render_baseball_journey(journey){
  var num_steps = journey.steps.length;
  var count_complete_steps = function(){
    return journey.steps.filter(
             function(step){return ! step.complete}
           ).length
  };

  var html = $("<div/>");
  var baseball_diamond = $("<div/>", {"class": "baseball-journey"})
  //add bases
  var bases_run = [false, false, false, false];
  $.each(bases_run, function(index, base_run){
    var base = $("<div/>", {"id": "base-"+index, "style": "visibility: hidden"})
    base.append("base-"+index)
    baseball_diamond.append(base);
  });

  //add paths
  /*
  $.each(bases_run, function(index, path){
    var path = $("<div/>", {"id": "path-"+index, "visibility": "hidden"})
    //set rotation and location
    baseball_diamond.append(path);
  });
  */

  //add tasks with handlers that update paths and bases and the next task
  var set_path_progress = function(){
    var full_path_len = 100;
    var percent_complete = count_complete_steps() / num_steps;
    for(var i = 0; i < 4; i++){
      var segment = min(0.25, percent_complete - (0.25*i));
      var len = segment / 0.25 * full_path_len;
      $("#path-"+i).attr('height', len);
    }
  };

  var set_base_progress = function(){
    var full_path_len = 100;
    var percent_complete = count_complete_steps() / num_steps;
    for(var i = 0; i < 4; i++){
      var base_run = percent_complete >= (0.25*(i+1));
      var visibility = base_run ? "visible" : "hidden";
      console.log(visibility);
      $("#base-"+i).css('visibility', visibility);
    }
  };

  html.append(baseball_diamond);

  var step_group = $("<div/>", {'class': "step_group"});
  var steps = journey.steps;
  $.each(steps, function(index, step){ 
    var step_html = $("<div/>", {"class": "journey-step", "id": "step-"+index});
    step_html.append((index+1) + ": "+ step.description)
    step_html.append($('<img src="check_mark.png" height=10 style="visibility: hidden" id=check-mark-'+index+'>'))
    var success_button = $('<button type="button" class="btn btn-default">Did it!</button>')
    success_button.click(function(){
      journey.steps[index].complete = ! journey.steps[index].complete;
      var cur_vis = $("#check-mark-"+index).css("visibility");
      $("#check-mark-"+index).css("visibility", cur_vis == "hidden"? "visible": "hidden");
      //set_path_progress();
      set_base_progress();
    });
    step_html.append(success_button)
    step_group.append(step_html);
  });
  html.append(step_group);
  return html
};
