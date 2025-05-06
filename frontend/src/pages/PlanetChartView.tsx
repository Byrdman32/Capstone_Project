import React, { useState, useMemo } from 'react';
import axios from 'axios';
import ScatterPlot from '../components/ScatterPlot';

interface Planet {
  name: string;
  mass: number;
  radius: number;
  orbital_period: number;
  semi_major_axis: number;
  eccentricity: number;
  [key: string]: number | string;
}

export const PlanetChartView: React.FC = () => {
  const [planets, setPlanets] = useState<Planet[]>([]);
  const [loading, setLoading] = useState(false);

  const [xField, setXField] = useState('mass');
  const [yField, setYField] = useState('radius');

  const [searchInput, setSearchInput] = useState('');
  const [error, setError] = useState<string | null>(null);

  const options = [
    { value: 'mass', label: 'Mass (M⊕)' },
    { value: 'radius', label: 'Radius (R⊕)' },
    { value: 'orbital_period', label: 'Orbital Period (days)' },
    { value: 'semi_major_axis', label: 'Semi-Major Axis (AU)' },
    { value: 'eccentricity', label: 'Eccentricity' }
  ];

  const fetchFilteredPlanets = async () => {
    setLoading(true);
    setError(null);

    try {
      const res = await axios.post('/api/planets/search', {
        request_string: searchInput
      });
      setPlanets(res.data);
    } catch (err: any) {
      const msg =
        err.response?.status === 400
          ? 'Invalid query syntax.'
          : 'Something went wrong.';
      setError(msg);
      setPlanets([]); // Clear old results if needed
    } finally {
      setLoading(false);
    }
  };

  const chartData = useMemo(() => {
    return planets
      .filter(p => typeof p[xField] === 'number' && typeof p[yField] === 'number')
      .map(p => ({
        x: p[xField] as number,
        y: p[yField] as number
      }));
  }, [planets, xField, yField]);

  return (
    <div>
      <h2>Compare Planet Attributes</h2>

      {/* Query Input */}
      <div style={{ marginBottom: '1rem' }}>
        <input
          style={{ width: '400px', marginRight: '1rem' }}
          type="text"
          placeholder='e.g. mass > 5 AND radius < 2'
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        />
        <button onClick={fetchFilteredPlanets}>Search</button>
      </div>

      {/* Optional Error Message */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Axis Dropdowns */}
      <div style={{ display: 'flex', gap: '1rem', marginBottom: '1rem' }}>
        <div>
          <label>X-Axis:</label><br />
          <select value={xField} onChange={e => setXField(e.target.value)}>
            {options.map(opt => <option key={opt.value} value={opt.value}>{opt.label}</option>)}
          </select>
        </div>
        <div>
          <label>Y-Axis:</label><br />
          <select value={yField} onChange={e => setYField(e.target.value)}>
            {options.map(opt => <option key={opt.value} value={opt.value}>{opt.label}</option>)}
          </select>
        </div>
      </div>

      {/* Chart Output */}
      {loading ? <p>Loading...</p> : (
        chartData.length > 0 ? (
          <ScatterPlot data={chartData} xLabel={xField} yLabel={yField} />
        ) : (
          <p>No data available for selected fields.</p>
        )
      )}
    </div>
  );
};