$(document).ready(function() {
    $('#add_item').click(function() {
      // Create a new <li> element with the text "Item"
      const newItem = $('<li>').text('Item');
      // Add the new <li> element to the <ul> element with the class "my_list"
      $('ul.my_list').append(newItem);
    });
  });
