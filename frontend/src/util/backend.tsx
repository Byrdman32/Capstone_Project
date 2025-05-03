import axios from 'axios'
import { useEffect, useState } from 'react'
interface MessageResponse {
    data: {
        message: string;
    };
}

function BackendCall() {
    const [message, setMessage] = useState<string>(''); // TypeScript enforces the type of the state variable

    useEffect(() => {
        axios.get('/api/stars') // Specify the expected response type
            .then((response: MessageResponse) => {
                console.log(response); // Log the message to the console
                setMessage(JSON.stringify(response.data)); // Update the message state variable with the result
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

export default BackendCall;
