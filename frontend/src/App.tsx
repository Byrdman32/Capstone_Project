import { useState, useEffect } from 'react'
import axios from 'axios'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

interface MessageResponse {
  data: {
    message: string;
  };
}

function BackendCall() {
  const [message, setMessage] = useState<string>(''); // TypeScript enforces the type of the state variable

  useEffect(() => {
    axios.get('/api/message') // Specify the expected response type
      .then((response: MessageResponse) => {
        setMessage(response.data.message); // Update the message state variable with the result
      })
      .catch((error: unknown) => {
        console.error(error);
      });
  }, []); // Empty dependency array ensures this runs only once when the component mounts

  return (
    <div>
      {message ? message : 'Loading...'} {/* Display a loading message until the API call completes */}
    </div>
  );
}

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <div>
        <h2>Backend Message</h2>
        <BackendCall /> {/* Call the BackendCall component to fetch and display the message */}
      </div>
    </>
  )
}

export default App
