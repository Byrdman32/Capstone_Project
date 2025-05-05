import { useEffect, useState } from 'react';
import { SearchBar } from "../components/SearchBar";
import { PlanetSearchCall } from '../util/backend';
import { ResultsContainer } from '../components/ResultsContainer';

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
                    <SearchBar placeholder="Search for a planet" onSearchResultChange={setSearchResult} searchFunction={PlanetSearchCall} />
                </div>
                <ResultsContainer
                    searchResult={searchResult}
                    title="Search Results"
                ></ResultsContainer>
            </div>
        </div>
    );
}