import { CountButton } from "../components/CountButton";
import { SearchBar } from "../components/SearchBar";

export function HomeView() {
    return (
        <div>
            <h1>Home Page</h1>
            <p>Welcome to the Exoplanet Dashboard!</p>
            <p>Filter/search bar</p>
            <SearchBar placeholder="Search for a planet" />
            <p>List of filtered results</p>
            <p>Each filtered result should have planet image and planet name, distance from earth, magnitude, discovery date, temperature, etc.</p>
            <p>Each filtered result should have a way to click to enter its individual planet page, for its ID</p>
            <div className="card">
                <CountButton />
                <p>
                    Edit <code>src/App.tsx</code> and save to test HMR
                </p>
            </div>
        </div>
    );
}