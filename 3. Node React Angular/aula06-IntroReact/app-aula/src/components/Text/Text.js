import React, { Component } from 'react'

export class Text extends Component {
  render() {
    return (
      <h1>
        { this.props.text }
      </h1>
    )
  }
}

export default Text
