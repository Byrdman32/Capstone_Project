import { useEffect, useState } from 'react';
import { SearchBar } from "../components/SearchBar";

interface Planet {
    [key: string]: any; // Allow additional dynamic properties
}

import './HomeView.css'; // Import the CSS file for styling

export function HomeView() {
    const [searchResult, setSearchResult] = useState<Planet[]>([]);
    useEffect(() => {
        if (searchResult) {
            console.log("Search result:", searchResult);
            console.log("Rendering result");
        }
    }, [searchResult]); // Dependency array to trigger effect when searchResult changes

    return (
        <div>
            <div className="home-container">
                <div className="search-bar-container">
                    <p>Planet Search</p>
                    <SearchBar placeholder="Search for a planet" onSearchResultChange={setSearchResult} />
                </div>
                <div className="results-container">
                    <h2>Search Results</h2>
                    {searchResult.length > 0 ? (
                        <ul>
                            {searchResult.map((planet: any, index: any) => (
                                <li key={index}>
                                    <ul>
                                        {Object.entries(planet).map(([key, value]) => (
                                            key !== "image" && ( // Exclude the image key from the list
                                                <li key={key}>
                                                    <strong>{key}:</strong> {String(value)}
                                                </li>
                                            )
                                        ))}
                                    </ul>
                                    <a href={`/planet/${planet.id}`}>View Details</a>
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p>No results found</p>
                    )}
                </div>
            </div>
        </div>
    );
}