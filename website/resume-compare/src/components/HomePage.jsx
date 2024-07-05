// HomePage.js

import React from 'react';
import { Link } from 'react-router-dom';

function HomePage(props) {
  return (
    <div>
      <h1>Select one of the option</h1>
      <br />
      <Link to="/User">
        <button>User Recommendation</button>
      </Link>
      <br />
      <br />    
      <Link to="/Hr">
        <button>HR comparison</button>
      </Link>
    </div>
  );
}

export default HomePage;
