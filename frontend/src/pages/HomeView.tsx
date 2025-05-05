import { useState } from 'react';
import { SearchBar } from "../components/SearchBar";
import { PlanetSearchCall } from '../util/backend';
import { ResultsContainer } from '../components/ResultsContainer';

import "./HomeView.css";

interface Planet {
    [key: string]: any; // Allow additional dynamic properties
}

export function HomeView() {
    const [searchResult, setSearchResult] = useState<Planet[]>([]);
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
                    showDetailsLink={true}
                ></ResultsContainer>
            </div>
        </div>
    );
}