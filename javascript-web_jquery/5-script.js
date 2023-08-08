$(document).ready(function() {
    $('div#add_item').on('click', function() {
      var listItem = $('<li>').text('Item');
      $('ul.my_list').append(listItem);
    });
  }); 