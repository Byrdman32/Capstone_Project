import React, { useEffect, useState } from 'react';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';
import SearchIcon from '@mui/icons-material/Search';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

interface SearchBarProps {
    placeholder: string;
    onSearchResultChange?: (result: any) => void; // Callback to pass search result to parent component
    searchFunction: (searchValue: string) => Promise<any>; // Function to call for search
}

export function SearchBar({ placeholder, onSearchResultChange, searchFunction }: SearchBarProps) {
    const [searchValue, setSearchValue] = useState<string>('');
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setSearchValue(event.target.value);
    }
    const [searchResult, setSearchResult] = useState<any>(null);
    const [searchError, setSearchError] = useState<any>(null);
    const handleKeyDown = async (event: React.KeyboardEvent) => {
        if (event.key === 'Enter') {
            setSearchResult(await searchFunction(searchValue)); // Update the state with the search result
        }
    }
    const handleReset = async () => {
        setSearchValue("");
        setSearchResult(await searchFunction(""));
    };
    useEffect(() => { // Computed property to watch search result and log when it changes
        if (searchResult) {
            if (searchResult.error) {
                setSearchError(searchResult.error);
                if (onSearchResultChange) {
                    onSearchResultChange([]);
                }
            } else {
                setSearchError(null);
                if (onSearchResultChange) {
                    onSearchResultChange(searchResult); // Pass the search result to the parent component
                }
            }
        }
    }, [searchResult]); // Dependency array to trigger effect when searchResult changes
    useEffect(() => {
        if (searchError) {
            console.error("Search error:", searchError);
        }
    }, [searchError]);
    useEffect(() => {
        const initialSearch = async () => {
            setSearchResult(await searchFunction(""));
        }
        initialSearch();
    }, [searchFunction]);
    return (
        <div>
            <TextField
                variant="outlined"
                placeholder={placeholder}
                fullWidth
                value={searchValue}
                onChange={handleChange}
                onKeyDown={handleKeyDown}
                sx={{
                    backgroundColor: '#fff',
                    borderRadius: '16px',
                }}
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
            <Button
                variant="contained"
                color="secondary"
                onClick={handleReset}
                style={{ marginTop: '8px', marginLeft: '8px' }}
            >
                Reset Search
            </Button>
            {searchError && (
                <Typography color="error" variant="body2" style={{ marginTop: '8px' }}>
                    {searchError}
                </Typography>
            )}
        </div>
    );
};