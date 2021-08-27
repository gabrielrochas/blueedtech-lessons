import { useState } from "react";

export default function Movie() {
  const [movies, setMovie] = useState([
    {
      id: 1,
      nome: "Capitan America: The First Avenger",
      imdb: "https://www.imdb.com/title/tt0458339/",
      imagemUrl:
        "https://m.media-amazon.com/images/M/MV5BMTYzOTc2NzU3N15BMl5BanBnXkFtZTcwNjY3MDE3NQ@@._V1_FMjpg_UX1000_.jpg",
    },
    {
      id: 2,
      nome: "Capitã Marvel",
      imdb: "https://www.imdb.com/title/tt4154664/",
      imagemUrl:
        "https://m.media-amazon.com/images/M/MV5BMTE0YWFmOTMtYTU2ZS00ZTIxLWE3OTEtYTNiYzBkZjViZThiXkEyXkFqcGdeQXVyODMzMzQ4OTI@._V1_FMjpg_UX1000_.jpg",
    },
    {
      id: 3,
      nome: "O incrivel Hulk",
      imdb: "https://www.imdb.com/title/tt0286716/",
      imagemUrl:
        "https://m.media-amazon.com/images/M/MV5BMzQwZDg1MGEtN2E5My00ZDJlLWI4MzItM2U2MjJhYzlkNmEzXkEyXkFqcGdeQXVyNDAxNjkxNjQ@._V1_FMjpg_UX1000_.jpg",
    },
    {
      id: 4,
      nome: "Iron Man",
      imdb: "https://www.imdb.com/title/tt0371746/",
      imagemUrl:
        "https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_FMjpg_UX1000_.jpg",
    },
    {
      id: 5,
      nome: "Iron Man 2",
      imdb: "https://www.imdb.com/title/tt1228705/",
      imagemUrl:
        "https://m.media-amazon.com/images/M/MV5BMTM0MDgwNjMyMl5BMl5BanBnXkFtZTcwNTg3NzAzMw@@._V1_FMjpg_UX1000_.jpg",
    }
  ]
  );
  const [movieName, setMovieName] = useState('');
  const [imdbMovie, setImdbMovie] = useState('');
  const [urlImg, setUrlMovie] = useState('');

  const addMovie = (e) => {
    e.preventDefault();
  }

  return (
    <div className="container">
      <h1>Movies</h1>
      <h3>New Movie</h3>
      <form >
        <input
          placeholder="New movie"
          type="text"
          value={movieName}
          onChange={(e) => setMovieName(e.target.value)}
        />
        <input
          placeholder="Imdb link"
          type="text"
          value={imdbMovie}
          onChange={(e) => setImdbMovie(e.target.value)}
        />
        <input
          placeholder="Img link"
          type="text"
          value={urlImg}
          onChange={(e) => setUrlMovie(e.target.value)}
        />
        <button type="submit">Save</button>
      </form>
      <ul>
        {movies.map((m, index) => (
          <li key={index}>
            <h5>{m.nome}</h5>
          </li>
        ))}
      </ul>
    </div>
  );
}
