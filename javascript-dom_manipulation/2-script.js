/* Task 2: Add `.red` class */
// Using document.querySelector to select the element with id 'red_header'
const redHeaderElement = document.querySelector('#red_header');

// Adding an event listener for a 'click' event on the redHeaderElement
redHeaderElement.addEventListener('click', function() {
  // Adding the class 'red' to the header element
  headerElement.classList.add('red');
});
