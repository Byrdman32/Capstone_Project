import { BackendCall } from "../util/backend";

export function AboutView() {
    return (
        <div>
            <h1>About Page</h1>
            <p>This is a dashboard for exploring exoplanets.</p>
            <p>Include meta-information, like our GitHub repository link, description of team/goals, etc.</p>
            <BackendCall />
        </div>
    );
}