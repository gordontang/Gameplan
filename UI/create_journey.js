$(document).ready(function(){
    var next = 1;
    $(".add-more").click(function(e){
        e.preventDefault();
        var addto = "#points" + next;
        var addRemove = "#points" + (next);
        next = next + 1;
        var newIn = '<input autocomplete="off" class="input" id="type' + next + '" name="type' + next + '" type="text" size="10"><input autocomplete="off" class="input" id="desc' + next + '" name="desc' + next + '" type="text" size="35"/><input autocomplete="off" class="input" id="link' + next + '" name="link' + next + '" type="text" size="20" /><input autocomplete="off" class="input" id="points' + next + '" name="points' + next + '" type="text" size=5/>';
        var newInput = $(newIn);
        var removeBtn = '<button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" >-</button></div><div id="field">';
        var removeButton = $(removeBtn);
        $(addto).after(newInput);
        $(addRemove).after(removeButton);
        $("#field" + next).attr('data-source',$(addto).attr('data-source'));
        $("#count").val(next);  
        
            $('.remove-me').click(function(e){
                e.preventDefault();
                var fieldNum = this.id.charAt(this.id.length-1);
                var fieldID = "#desc" + fieldNum;
                $(this).remove();
                $("#type" + fieldNum).remove();
                $("#link" + fieldNum).remove();
                $("#points" + fieldNum).remove();
                $(fieldID).remove();
            });
    });
    

    
});

