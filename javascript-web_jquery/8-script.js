$(document).ready(function() {
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
      var movies = data.results;
      var listMovies = '';
      for (var i = 0; i < movies.length; i++) {
        var title = movies[i].title;
        listMovies += '<li>' + title + '</li>';
      }
      $('#list_movies').html(listMovies);
    });
  });