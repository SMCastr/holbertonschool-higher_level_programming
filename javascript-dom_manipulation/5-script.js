/* Task 5: Change the text */
// Using document.querySelector to select the element with id 'update_header'
const updateHeaderElement = document.querySelector('#update_header');

// Adding an event listener for a 'click' event on the updateHeaderElement
updateHeaderElement.addEventListener('click', function() {
  // Setting the text content of the header element to 'New Header!!!'
  headerElement.textContent = 'New Header!!!';
});
