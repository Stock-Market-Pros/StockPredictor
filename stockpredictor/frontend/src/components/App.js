import React from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/header';
import View from './stocks/view';

class App extends React.Component {

  render() {
    return(
      <div>
        <Header />
        <View />
      </div>
    )
  }
}

export default App;