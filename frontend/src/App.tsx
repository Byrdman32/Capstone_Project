import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import BackendCall from './util/backend';
import { HomeView } from './pages/HomeView';
import { IndividualPlanetView } from './pages/IndividualPlanetView';
import { AboutView } from './pages/AboutView';

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