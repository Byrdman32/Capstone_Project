import { useState } from 'react';

export function CountButton() {
    const [count, setCount] = useState(0);

    return (
        <button onClick={() => setCount((count) => count + 1)}>
            Example button: count is {count}
        </button>
    );
}