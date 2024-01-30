/* Task 4: List of elements */
// Using document.querySelector to select the element with id 'add_item'
const addItemElement = document.querySelector('#add_item');

// Adding an event listener for a 'click' event on the addItemElement
addItemElement.addEventListener('click', function() {
  // Using document.createElement to create a new 'li' element
  const newListItem = document.createElement('li');
  // Setting the text content of the new 'li' element
  newListItem.textContent = 'Item';
  // Using document.querySelector to select the 'ul' element with class 'my_list'
  const myListElement = document.querySelector('.my_list');
  // Appending the new 'li' element to the 'ul' element
  myListElement.appendChild(newListItem);
});
