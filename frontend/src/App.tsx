import { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import BackendCall from './util/backend';

function HomeView() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h1>Home Page</h1>
      <p>Welcome to the Exoplanet Dashboard!</p>
      <p>Filter/search bar</p>
      <p>List of filtered results</p>
      <p>Each filtered result should have planet image and planet name, distance from earth, magnitude, discovery date, temperature, etc.</p>
      <p>Each filtered result should have a way to click to enter its individual planet page, for its ID</p>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          Example button: count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
    </div>
  );
}

function IndividualPlanetView() {
  return (
    <div>
      <h1>Individual Planet Page</h1>
      <p>This is a detailed view of an individual exoplanet.</p>
      <p>This should show the same information as the summary in the home view, with more detail</p>
      <p>Also include any relevant charts generated from the back-end (e.g. scatter plots, comparisons to Earth)</p>
      <p>Also include LLM-generated description of the planet, possibly with some embellishment</p>
      <p>Also calculate and include a list of similar planets - something like Manhattan distance of normalized attributes</p>
    </div>
  );
}

function AboutView() {
  return (
    <div>
      <h1>About Page</h1>
      <p>This is a dashboard for exploring exoplanets.</p>
      <p>Include meta-information, like our GitHub repository link, description of team/goals, etc.</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link> | <Link to="/planet/:id">Individual Planet</Link> | <Link to="/about">About</Link> | <Link to="/backend">Backend Message</Link>
      </nav>
      <Routes>
        <Route path="/" element={<HomeView />} />
        <Route path="/planet/:id" element={<IndividualPlanetView />} />
        <Route path="/about" element={<AboutView />} />
        <Route path="/backend" element={<BackendCall />} />
      </Routes>
    </Router>
  );
}

export default App;