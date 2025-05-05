import axios from 'axios'
import { useEffect, useState } from 'react'
interface Response {
    data: {
        message: string;
    };
}

export function BackendCall() {
    const [message, setMessage] = useState<string>(''); // TypeScript enforces the type of the state variable

    useEffect(() => {
        axios.get('/api/stars') // Specify the expected response type
            .then((response: Response) => {
                console.log(response); // Log the message to the console
                setMessage(JSON.stringify(response.data.message)); // Update the message state variable with the result
            })
            .catch((error: unknown) => {
                console.error(error);
            });
    }, []); // Empty dependency array ensures this runs only once when the component mounts

    return (
        <div>
            {message ? message : 'Loading...'} {/* Display a loading message until the API call completes */}
        </div>
    );
}

export async function SystemSearchCall(searchQuery: string): Promise<any> {
    try {
        if (!searchQuery) {
            searchQuery = "ID > 0";
        }
        const response = await axios.post(
            '/api/systems/search',
            { request_string: searchQuery },
        );
        return response.data; // Properly return the response
    } catch (error: any) {
        return error.response.data;
    }
}

export async function PlanetSearchCall(searchQuery: string): Promise<any> {
    try {
        if (!searchQuery) {
            searchQuery = "ID > 0";
        }
        const response = await axios.post(
            '/api/planets/search',
            { request_string: searchQuery },
        );
        return response.data; // Properly return the response
    } catch (error: any) {
        return error.response.data;
    }
}
