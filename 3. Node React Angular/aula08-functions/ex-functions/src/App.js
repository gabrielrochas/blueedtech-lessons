import React, { Component } from "react";
import Count from './components/Count';
import Movie from './components/Movies';

export default class App extends Component {
  render() {
    return (
      <div>
        <Count />
        <Movie />
      </div>
    );
  }
}
