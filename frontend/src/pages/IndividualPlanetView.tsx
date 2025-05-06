import { useState, useEffect } from 'react';
import { useParams, useNavigate } from "react-router-dom";
import { PlanetSearchCall } from '../util/backend';
import { IndividualResultContainer } from '../components/IndividualResultContainer';
import PlanetAIDescription from '../components/PlanetAIDescription';

import "./IndividualPlanetView.css";

export function IndividualPlanetView() {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const [planetName, setPlanetName] = useState<string | null>(null);
    const [searchResult, setSearchResult] = useState<any[]>([]);
    const [isLoading, setIsLoading] = useState<boolean>(true); // Track loading state

    useEffect(() => {
        if (id) {
            setIsLoading(true); // Set loading state to true
            PlanetSearchCall(`ID = ${id}`).then((result) => {
                setSearchResult(result);
                if (result.length === 1 && result[0].planet_name) {
                    setPlanetName(result[0].planet_name);
                } else {
                    setPlanetName(`Planet ${id}`);
                }
            }).catch((error) => {
                console.error("Error fetching planet data:", error);
            }).finally(() => {
                setIsLoading(false); // Set loading state to false
            });
        }
    }, [id]);

    const handleNextPlanet = () => {
        const nextId = parseInt(id || "0", 10) + 1; // Increment the current ID
        setPlanetName(null); // Reset planet name
        setSearchResult([]); // Clear previous search results
        navigate(`/planet/${nextId}`); // Navigate to the next planet
    };

    const handlePreviousPlanet = () => {
        const prevId = Math.max(parseInt(id || "0", 10) - 1, 1); // Decrement the current ID, ensuring it doesn't go below 1
        setPlanetName(null); // Reset planet name
        setSearchResult([]); // Clear previous search results
        navigate(`/planet/${prevId}`); // Navigate to the previous planet
    };

    return (
        <div>
            {isLoading ? (
                <h2>Loading...</h2> // Show loading message while fetching data
            ) : (
                <>
                    <h2>{planetName}</h2>
                    <div className="individual-planet-container">
                        <div className="planet-description">
                            <PlanetAIDescription planetId={id} />
                        </div>
                        <IndividualResultContainer
                            searchResult={searchResult}
                            title=""
                            showDetailsLink={false}
                        ></IndividualResultContainer>
                    </div>
                </>
            )}
            <button className="previous-planet-button" onClick={handlePreviousPlanet}>
                Previous Planet
            </button>
            <button className="next-planet-button" onClick={handleNextPlanet}>
                Next Planet
            </button>
        </div>
    );
}