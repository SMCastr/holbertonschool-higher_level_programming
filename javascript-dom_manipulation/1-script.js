/* Task 1: Click and turn red */
// Using document.querySelector to select the element with id 'red_header'
const redHeaderElement = document.querySelector('#red_header');

// Adding an event listener for a 'click' event on the redHeaderElement
redHeaderElement.addEventListener('click', function() {
  // Updating the text color of the header element to red (#FF0000)
  headerElement.style.color = '#FF0000';
});
