import { useParams } from "react-router-dom";

export function IndividualPlanetView() {
    const { id } = useParams<{ id: string }>();
    return (
        <div>
            <h2>Planet ID: {id}</h2>
            <p>This is a detailed view of an individual exoplanet.</p>
            <p>This should show the same information as the summary in the home view, with more detail</p>
            <p>Also include any relevant charts generated from the back-end (e.g. scatter plots, comparisons to Earth)</p>
            <p>Also include LLM-generated description of the planet, possibly with some embellishment</p>
            <p>Also calculate and include a list of similar planets - something like Manhattan distance of normalized attributes</p>
        </div>
    );
}