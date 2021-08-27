import React from 'react';
import './App.css';

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      filmes: [
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
        },
      ],
    };
  }
  
  render() {
    const { filmes } = this.state;
    return (
      <div className="container">
        
        {filmes.map((filme) => (
          <div className="card" key={filme.id}>
            <img src={filme.imagemUrl} alt="Avatar" />
            <div className="card-container">
              <h4>
                <b>{filme.nome}</b>
              </h4>
              <a href={filme.imdb} target="blank">
                IMDB
              </a>
            </div>
          </div>
        ))}
      </div>
    );
  }
}
