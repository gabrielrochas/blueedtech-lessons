// Import Express
const express = require('express');
const app = express();

// Define PORT
const PORT = 3001;
 
app.use(express.json());

const movies = [
  'O Poderoso Chefão',
  'O Senhor dos Anéis',
  'Meu Malvado Favorito',
  'Titanic',
];

// Random number
const randomNum = (min, max) => Math.floor(Math.random() * (max - min) + min);

// GET to Home
app.get('/', (req, res) => {
  res.send("Welcome to Aroeira Flix!");
});

// GET all items in movies list
app.get('/movies', (req, res) => {
  res.send(movies);
});

// GET movie by 'id'
app.get('/movies/:id', (req, res) => {
  const id = req.params.id - 1;
  checkMovie(id, res);
  const movie = movies[id];
  res.send(movie);
});

// POST a new movie
app.post('/movies', (req, res) => {
  const movie = req.body.movie;
  movies.push(movie);
  res.send(`Movie ${movie} succesfuly added to the list`);
});

// UPDATE movie
app.put('/movies/:id', (req, res) => {
  const id = req.params.id - 1;
  checkMovie(id, res);
  const newMovie = req.body.movie;
  const oldMovie = movies[id];
  movies[id] = newMovie;
  res.send(`Movie ${oldMovie} successfuly updated to ${newMovie}`)
});

// DELETE movie
app.delete('/movies/:id', (req, res) => {
  const id = req.params.id-1;
  checkMovie(id, res);
  const movie = movies[id]
  delete(movies[id]);
  res.send(`Movie ${movie} successfuly deleted!`)
});


app.listen(PORT, () => {
  console.info(`Serve up and running in url: http://localhost:${PORT}`)
});

// Check if movie exist
function checkMovie(id, res) {
  if (!movies[id])
    res.send('No such movie');
}
