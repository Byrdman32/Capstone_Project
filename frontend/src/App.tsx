import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import { HomeView } from './pages/HomeView';
import { IndividualPlanetView } from './pages/IndividualPlanetView';
import { AboutView } from './pages/AboutView';
import { PlanetChartView } from './pages/PlanetChartView';

function App() {
  return (
    <div className="App">
      <Router>
        <header className="App-header">
          <h1>Exoplanet Dashboard</h1>
          <nav>
            <Link to="/">Home</Link> |{" "}
            <Link to="/chart">Chart</Link> |{" "}
            <Link to="/about">About</Link>{" "}
          </nav>
        </header>
        <Routes>
          <Route path="/" element={<HomeView />} />
          <Route path="/planet/:id" element={<IndividualPlanetView />} />
          <Route path="/about" element={<AboutView />} />
          <Route path="/chart" element={<PlanetChartView />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;