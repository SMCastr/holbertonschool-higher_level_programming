/* Task 7: Star Wars movies */
// Using document.querySelector to select the element with id 'list_movies'
const listMoviesElement = document.querySelector('#list_movies');

// Fetching and listing the titles for all movies from the specified URL using the Fetch API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Checking if the response status is OK (status code 200)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Parsing the JSON data from the response
    return response.json();
  })
  .then(data => {
    // Looping through each movie and adding its title to the list
    data.results.forEach(movie => {
      // Using document.createElement to create a new 'li' element
      const newListItem = document.createElement('li');
      // Setting the text content of the new 'li' element to the movie title
      newListItem.textContent = movie.title;
      // Appending the new 'li' element to the 'ul' element
      listMoviesElement.appendChild(newListItem);
    });
  })
  .catch(error => {
    // Handling errors
    console.error('Error fetching data:', error);
  });
