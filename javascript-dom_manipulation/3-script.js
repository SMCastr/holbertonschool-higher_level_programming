/* Task 3: Toggle classes */
// Using document.querySelector to select the element with id 'toggle_header'
const toggleHeaderElement = document.querySelector('#toggle_header');

// Adding an event listener for a 'click' event on the toggleHeaderElement
toggleHeaderElement.addEventListener('click', function() {
  // Toggling the class 'red' on the header element
  headerElement.classList.toggle('red');
  // Toggling the class 'green' on the header element
  headerElement.classList.toggle('green');
});
