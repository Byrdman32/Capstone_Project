import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import { HomeView } from './pages/HomeView';
import { IndividualPlanetView } from './pages/IndividualPlanetView';
import { AboutView } from './pages/AboutView';

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link> | <Link to="/planet/:id">Individual Planet</Link> | <Link to="/about">About</Link>
      </nav>
      <Routes>
        <Route path="/" element={<HomeView />} />
        <Route path="/planet/:id" element={<IndividualPlanetView />} />
        <Route path="/about" element={<AboutView />} />
      </Routes>
    </Router>
  );
}

export default App;