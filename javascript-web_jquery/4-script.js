$(document).ready(function() {
    $('div#toggle_header').on('click', function() {
      var headerElement = $('header');
      if (headerElement.hasClass('red')) {
        headerElement.removeClass('red').addClass('green');
      } else if (headerElement.hasClass('green')) {
        headerElement.removeClass('green').addClass('red');
      } else {
        headerElement.addClass('red');
      }
    });
  });