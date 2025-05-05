import { useState, useEffect, useRef } from 'react';
import Spinner from './Spinner';

const PlanetAIDescription = ({ planetId }: any) => {
    const [description, setDescription] = useState('');
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);
    const hasFetched = useRef(false); // Track if fetch has already been initiated

    useEffect(() => {
        if (hasFetched.current) return; // Prevent multiple fetches for a planet ID
        hasFetched.current = true;

        const fetchDescription = async () => {
            try {
                const response = await fetch(`/api/planets/${planetId}/ai_description`);
                if (!response.ok) {
                    throw new Error(`Error: ${response.status} - ${response.statusText}`);
                }
                const data = await response.json();
                setDescription(data.description);
            } catch (err: any) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchDescription();
    }, [planetId]);

    if (loading) return <Spinner />;
    if (error) return <p>Error: {error}</p>;

    return (
        <div>
            <p>{description}</p>
        </div>
    );
};

export default PlanetAIDescription;