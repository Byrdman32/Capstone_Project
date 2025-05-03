import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';
import SearchIcon from '@mui/icons-material/Search';
import { PlanetSearchCall } from '../util/backend';

interface SearchBarProps {
    placeholder: string;
}

export function SearchBar({ placeholder }: SearchBarProps) {
    const [searchValue, setSearchValue] = useState<string>('');
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchValue(event.target.value);
    }
    const handleKeyDown = (event: React.KeyboardEvent) => {
        if (event.key === 'Enter') {
            // Handle search action here, e.g., call a search function or update state
            console.log('Search value:', searchValue);
            PlanetSearchCall(searchValue); // Call the backend function with the search value
        }
    }
    return (
        <TextField
            variant="outlined"
            placeholder={placeholder}
            fullWidth
            value={searchValue}
            onChange={handleChange}
            onKeyDown={handleKeyDown}
            slotProps={{
                input: {
                    startAdornment: (
                        <InputAdornment position="start">
                            <SearchIcon />
                        </InputAdornment>
                    ),
                },
            }}
        />
    );
};