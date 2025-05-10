import React from 'react';
import {
  ResponsiveContainer,
  ScatterChart,
  Scatter,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip
} from 'recharts';

type DataPoint = {
  x: number;
  y: number;
};

interface ScatterPlotProps {
  data: DataPoint[];
  xLabel?: string;
  yLabel?: string;
}

const ScatterPlot: React.FC<ScatterPlotProps> = ({ data, xLabel = 'X', yLabel = 'Y' }) => {
  return (
    <div style={{ width: '100%', height: 400 }}>
      <ResponsiveContainer>
        <ScatterChart>
          <CartesianGrid />
          <XAxis
            type="number"
            dataKey="x"
            name={xLabel}
            label={{ value: xLabel, position: 'insideBottomRight', offset: -5 }}
          />
          <YAxis
            type="number"
            dataKey="y"
            name={yLabel}
            label={{ value: yLabel, angle: -90, position: 'insideLeft' }}
          />
          <Tooltip cursor={{ strokeDasharray: '3 3' }} />
          <Scatter name="Planets" data={data} fill="#8884d8" />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ScatterPlot;