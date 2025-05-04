import { useEffect, useState } from 'react';
import { CountButton } from "../components/CountButton";
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
            <h1>Home Page</h1>
            <p>Welcome to the Exoplanet Dashboard!</p>
            <p>Filter/search bar</p>
            <SearchBar placeholder="Search for a planet" onSearchResultChange={setSearchResult} />
            <p>List of filtered results</p>
            <div>
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
            <p>Each filtered result should have planet image and planet name, distance from earth, magnitude, discovery date, temperature, etc.</p>
            <p>Each filtered result should have a way to click to enter its individual planet page, for its ID</p>
            <div className="card">
                <CountButton />
                <p>
                    Edit <code>src/App.tsx</code> and save to test HMR
                </p>
            </div>
        </div>
    );
}