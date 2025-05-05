import React from "react";
import { toCapitalCase, removeUnderscores } from "../util/formatting";

import "./ResultsContainer.css";

interface ResultsContainerProps {
    searchResult: Array<any>;
    title: string;
    showDetailsLink: boolean;
}

export const IndividualResultContainer: React.FC<ResultsContainerProps> = ({ searchResult, title, showDetailsLink }) => {
    return (
        <div className="individual-result-container">
            <h2>{title}</h2>
            {searchResult.length === 1 && (
                <div className="single-result">
                    <div className="result-item">
                        <div className="image-column">
                            {searchResult[0].radius && searchResult[0].radius > 10 && (
                                <img
                                    src={`/exoplanets/large/${(searchResult[0].id % 14) + 1}.png`} // This needs to be manually updated for the number of large exoplanet images
                                    alt={`Hypothetical exoplanet image`}
                                    className="planet-image"
                                />
                            )}
                            {(!searchResult[0].radius || searchResult[0].radius <= 10) && (
                                <img
                                    src={`/exoplanets/small/${(searchResult[0].id % 14) + 1}.png`} // This needs to be manually updated for the number of small exoplanet images
                                    alt={`Hypothetical exoplanet image`}
                                    className="planet-image"
                                />
                            )}

                        </div>
                        <div className="individual-details-column">
                            <ul>
                                {Object.entries(searchResult[0]).map(([key, value]) => (
                                    key !== "image" && ( // Exclude the image key from the list
                                        <li key={key}>
                                            <strong>{toCapitalCase(removeUnderscores(key))}:</strong> {String(removeUnderscores(String(value)))}
                                        </li>
                                    )
                                ))}
                            </ul>
                        </div>
                        {showDetailsLink && (
                            <a href={`/planet/${searchResult[0].id}`} className="details-link">View Details</a>
                        )}

                    </div>
                </div>
            )}
        </div>
    );
};