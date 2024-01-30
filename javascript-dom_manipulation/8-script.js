/* Task 8: Say Hello! */
// Using document.querySelector to select the element with id 'hello'
const helloElement = document.querySelector('#hello');

// Fetching the translation of "hello" from the specified URL using the Fetch API
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    // Checking if the response status is OK (status code 200)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Parsing the JSON data from the response
    return response.json();
  })
  .then(data => {
    // Setting the text content of the hello element to the translated "hello"
    helloElement.textContent = data.hello;
  })
  .catch(error => {
    // Handling errors
    console.error('Error fetching data:', error);
  });
