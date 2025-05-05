import { useState, useEffect } from 'react';
import { useParams } from "react-router-dom";
import { PlanetSearchCall } from '../util/backend';
import { IndividualResultContainer } from '../components/IndividualResultContainer';
import PlanetAIDescription from '../components/PlanetAIDescription';

import "./IndividualPlanetView.css";

export function IndividualPlanetView() {
    const { id } = useParams<{ id: string }>();
    const [planetName, setPlanetName] = useState<string | null>(null);
    const [searchResult, setSearchResult] = useState<any[]>([]);

    useEffect(() => { // When ID changes (navigating to page for some ID), fetch that planet's data
        if (id) {
            PlanetSearchCall(`ID = ${id}`).then((result) => {
                setSearchResult(result);
                if (result.length === 1 && result[0].planet_name) {
                    setPlanetName(result[0].planet_name);
                } else {
                    setPlanetName(`Planet ${id}`);
                }
            }).catch((error) => {
                console.error("Error fetching planet data:", error);
            });
        }
    }, [id]);

    return (
        <div>
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
        </div>
    );
}