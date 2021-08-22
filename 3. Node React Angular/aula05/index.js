const express = require('express');
const app = express();

const PORT = 3000;

app.use(express.json());

const movies = [
  {
    id: 1,
    title: 'The Lord of The Rings',
    imgUrl: 'https://media.fstatic.com/SFp4c8GT3GTGYok7_526qDSHTns=/290x478/smart/media/movies/covers/2018/09/66432b37ed80464274a58239b695007f95c79155.jpg'
  },
  {
    id: 2,
    title: 'Harry Potter',
    imgUrl: 'https://media.fstatic.com/SFp4c8GT3GTGYok7_526qDSHTns=/290x478/smart/media/movies/covers/2018/09/66432b37ed80464274a58239b695007f95c79155.jpg'
  },
  {
    id: 3,
    title: 'O Auto da Compadecida',
    imgUrl: 'https://media.fstatic.com/SFp4c8GT3GTGYok7_526qDSHTns=/290x478/smart/media/movies/covers/2018/09/66432b37ed80464274a58239b695007f95c79155.jpg'
  },
];

// Index route
app.get('/', (req, res) => {
  res.send('Welcome to movies app');
});

// GET Movies
const getValidMovies = () => movies.filter(Boolean);
// GET movie by id
const getMovieById = (id) => getValidMovies().find((movie) => movie.id == id);
// GET movie by array index 
constIndexByMovie = (id) => findIndex((movie) => movie.id === id)

// Route to get all movies
app.get('/movies', (req, res) => {
  res.send(getValidMovies())
} );

// Movie by ID route
app.get('/movies/:id', (req, res) => {
  const id = req.params.id - 1;
  const movie = getMovieById(id)
  if(!movie) {
    res.send('No such movie')
  }
  res.send(movie)
});

// Route do add new movie
app.post('/movies', (req, res) => {
  const movie = req.body;

  if(!movie || !movie.title || !movie.imgUrl) {
    res.status(400).send({
      message: 'Invalid movie. Try again.'
    });
    return;
  }
  const lastMovie = movies[movies.length - 1];

  if(movies.length) {
    movie.id = lastMovie.id + 1; 
    movies.push(movie)
  }
  else {
    movie.id = 1;
    movies.push(movie)
  }

  res.send(`Movie ${movie.title} successfuly added on id ${movie.id}!`)
});

// Route to update a movie
app.put('/movies/:id', (req, res) => {
  const id = req.params.id-1;
  const movieIndex = getIndexByMovie(id);
  
  if(movieIndex < 0) {
    res.status(404).send({
      message: "No such movie. Try again."
    })
  }

  const updateMovie = req.body;

  if(!Object.keys(updateMovie).length) {
    res.status(400).send({
      message: "Body empty"
    });
    return;
  }
  if(!updateMovie || !updateMovie.title || !updateMovie.imgUrl) {
    res.status(400).send({
      message: "Invalid movie"
    });
    return;
  }

  const movie = getMovieById(id);

  movies[movieIndex] = {
    ...movie,
    ...updateMovie
  };
  

  res.send(`Movie updated ${movie}`)
});

// Route do delete a movie
app.delete('/movies/:id', (req, res) => {
  const id = +req.params.id;

  const indexMovie = getIndexByMovie(id);

  if(indexMovie < 0) {
    res.status(404).send({
      message: "No such movie"
    });
  }

  movies.splice(indexMovie, 1);
  res.send({
    message: "Movie successfuly deleted!",
  });
});

app.listen(PORT, function() {
  console.info(`App runnig at port http://localhost:${PORT}`)
});