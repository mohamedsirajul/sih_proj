$(".input_text").focus(function(){
    $(this).prev('.fa').addclass('glowIcon')
})
$(".input_text").focusout(function(){
    $(this).prev('.fa').removeclass('glowIcon')
})

  $(document).ready(function() {
    $("#submit_button").click(function() {
      // Redirect to Dashboard.html when the submit button is clicked
      window.location.href = "Dashboard.html";
    });
  });
