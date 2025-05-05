import { useEffect, useState } from 'react';
import { SearchBar } from "../components/SearchBar";

interface Planet {
    [key: string]: any; // Allow additional dynamic properties
}

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
                    <h2>Planet Search</h2>
                    <SearchBar placeholder="Search for a planet" onSearchResultChange={setSearchResult} />
                </div>
                <div className="results-container">
                    <h2>Search Results</h2>
                    {searchResult.length > 0 ? (
                        <ul>
                            {searchResult.map((planet: any, index: any) => (
                                <li key={index} className="result-item">
                                    <div className="image-column">
                                        <img
                                            src={`exoplanets/${(planet.id % 5) + 1}.png`}
                                            alt={`Hypothetical exoplanet image`}
                                            className="planet-image"
                                        />
                                    </div>
                                    <div className="details-column">
                                        <ul>
                                            {Object.entries(planet).map(([key, value]) => (
                                                key !== "image" && ( // Exclude the image key from the list
                                                    <li key={key}>
                                                        <strong>{key}:</strong> {String(value)}
                                                    </li>
                                                )
                                            ))}
                                        </ul>
                                    </div>
                                    <a href={`/planet/2`}>View Details</a>
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