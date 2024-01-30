/* Task 6: Star Wars character */
// Using document.querySelector to select the element with id 'character'
const characterElement = document.querySelector('#character');

// Fetching the character name from the specified URL using the Fetch API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Checking if the response status is OK (status code 200)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Parsing the JSON data from the response
    return response.json();
  })
  .then(data => {
    // Setting the text content of the character element to the fetched character name
    characterElement.textContent = data.name;
  })
  .catch(error => {
    // Handling errors
    console.error('Error fetching data:', error);
  });
