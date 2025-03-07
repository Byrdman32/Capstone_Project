import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

function BackendCall() {
  const [message, setMessage] = useState('');
  // Initializes the message state variable, which can be updated with setMessage
  //  Any other component using message will be updated when setMessage is called
  //  useState('') initializes the message as empty
  useEffect(() => {
    axios.get('/api/message')
      .then(response => {
        setMessage(response.data.message); // Update the message state variable with the result
      })
      .catch(error => {
        console.error(error);
      });
  }, []); // Uses a hook effect - a hook causes side effects, which can affect things outside of the component
  // By default, a hook effect runs whenever rendered

  return (
    <div>
      {message}
    </div>
  );
} // Like any other component, this is a function that returns JSX (HTML-like)

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hello world!
          Making a backend API call: <BackendCall />
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
