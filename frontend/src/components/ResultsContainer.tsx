import React, { useState, useEffect } from "react";
import Button from '@mui/material/Button';

import "./ResultsContainer.css";

interface ResultsContainerProps {
    searchResult: Array<any>;
    title: string;
    showDetailsLink: boolean;
}

export const ResultsContainer: React.FC<ResultsContainerProps> = ({ searchResult, title, showDetailsLink }) => {
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 3;

    // Calculate total pages
    const totalPages = Math.ceil(searchResult.length / itemsPerPage);

    useEffect(() => { // Ensure current page is always valid
        if (currentPage < Math.min(1, totalPages) || currentPage > totalPages) {
            if (currentPage > totalPages) {
                setCurrentPage(totalPages);
            } else {
                setCurrentPage(1);
            }
        }
    }, [totalPages, currentPage]);

    // Get the results for the current page
    const paginatedResults = searchResult.slice(
        (currentPage - 1) * itemsPerPage,
        currentPage * itemsPerPage
    );

    // Handle page change
    const handlePageChange = (page: number) => {
        if (page >= 1 && page <= totalPages) {
            setCurrentPage(page);
        }
    };

    return (
        <div className="results-container">
            <h2>{title}</h2>
            {paginatedResults.length > 0 ? (
                <ul>
                    {paginatedResults.map((planet: any, index: number) => (
                        <li key={index} className="result-item">
                            <div className="image-column">
                                <img
                                    src={`/exoplanets/${(planet.id % 20) + 1}.png`} // This needs to be manually updated for the number of exoplanet images
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
                            {showDetailsLink && (
                                <a href={`/planet/${planet.id}`} className="details-link">View Details</a>
                            )}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No results found</p>
            )}

            {/* Pagination Controls */}
            {totalPages > 1 && (
                <div className="pagination-controls">
                    <Button
                        onClick={() => handlePageChange(currentPage - 1)}
                        disabled={currentPage === 1}
                        className="pagination-prev-button"
                        variant="contained"
                        color="secondary"
                        sx={{
                            display: currentPage === 1 ? 'none' : 'inline-block',
                        }}
                    >
                        Previous
                    </Button>
                    <span className="pagination-message">
                        Page {currentPage} of {totalPages}
                    </span>
                    <Button
                        onClick={() => handlePageChange(currentPage + 1)}
                        disabled={currentPage === totalPages}
                        className="pagination-next-button"
                        variant="contained"
                        color="secondary"
                        sx={{
                            display: currentPage === totalPages ? 'none' : 'inline-block',
                        }}
                    >
                        Next
                    </Button>
                </div>
            )}
        </div>
    );
};