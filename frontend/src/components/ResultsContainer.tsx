import React, { useState, useEffect } from "react";
import "./ResultsContainer.css";

interface ResultsContainerProps {
    searchResult: Array<any>;
    title: string;
}

export const ResultsContainer: React.FC<ResultsContainerProps> = ({ searchResult, title }) => {
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 3;

    // Calculate total pages
    const totalPages = Math.ceil(searchResult.length / itemsPerPage);

    useEffect(() => { // Ensure current page is always valid
        if (currentPage > totalPages) {
            setCurrentPage(totalPages);
        } else if (currentPage < 1) {
            setCurrentPage(1);
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

            {/* Pagination Controls */}
            <div className="pagination-controls">
                <button
                    onClick={() => handlePageChange(currentPage - 1)}
                    disabled={currentPage === 1}
                    className="pagination-prev-button"
                >
                    Previous
                </button>
                <span className="pagination-message">
                    Page {currentPage} of {totalPages}
                </span>
                <button
                    onClick={() => handlePageChange(currentPage + 1)}
                    disabled={currentPage === totalPages}
                    className="pagination-next-button"
                >
                    Next
                </button>
            </div>
        </div>
    );
};