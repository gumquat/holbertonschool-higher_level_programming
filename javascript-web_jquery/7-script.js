$(document).ready(function() {
    $.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
      var characterName = data.name;
      $('#character').text(characterName);
    });
  });