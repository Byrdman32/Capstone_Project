import { useState, useEffect } from 'react';
import { useParams } from "react-router-dom";
import { PlanetSearchCall } from '../util/backend';
import { ResultsContainer } from '../components/ResultsContainer';

import "./IndividualPlanetView.css";

export function IndividualPlanetView() {
    const { id } = useParams<{ id: string }>();
    const [searchResult, setSearchResult] = useState<any[]>([]);

    useEffect(() => { // When ID changes (navigating to page for some ID), fetch that planet's data
        if (id) {
            PlanetSearchCall(`ID = ${id}`).then((result) => {
                setSearchResult(result);
            }).catch((error) => {
                console.error("Error fetching planet data:", error);
            });
        }
    }, [id]);

    return (
        <div>
            <h2>Planet ID: {id}</h2>
            <div className="individual-planet-container">
                <div className="planet-description">
                    <p>This is a detailed view of an individual exoplanet.</p>
                    <p>This should show the same information as the summary in the home view, with more detail</p>
                    <p>Also include any relevant charts generated from the back-end (e.g. scatter plots, comparisons to Earth)</p>
                    <p>Also include LLM-generated description of the planet, possibly with some embellishment</p>
                    <p>Also calculate and include a list of similar planets - something like Manhattan distance of normalized attributes</p>
                </div>
                <ResultsContainer
                    searchResult={searchResult}
                    title=""
                    showDetailsLink={false}
                ></ResultsContainer>
            </div>
        </div>
    );
}