import { useState } from 'react';

export function HomeView() {
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