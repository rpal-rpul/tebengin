$(document).ready(function() {
  var formFields = $('.input-wrapper');

  formFields.each(function() {
    var field = $(this);
    var input = field.find('input');
    var label = field.find('label');
    var icon = field.find('i');
    
    function checkInput() {
      var valueLength = input.val().length;
      
      if (valueLength > 0 ) {
        label.addClass('focus')
        icon.addClass('focus-icon')
      } else {
            label.removeClass('focus')
            icon.removeClass('focus-icon')
      }
    }
    
    input.change(function() {
      checkInput()
    })
  });
});