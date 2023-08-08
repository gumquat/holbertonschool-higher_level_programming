$(document).ready(function() {
    $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function(data) {
      var helloValue = $(data).find('#hello').text();
      $('#hello').text(helloValue);
    });
  });