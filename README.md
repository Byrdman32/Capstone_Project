```markdown
Development workflow:

To set up the API token, get our API token from the Discord server, then copy it to a file `backend/backend_modules/tokens/api_token`.

## Open in full dev container view or as interactive terminal:
### Dev container:
- In VS Code: `Ctrl + Shift + P` -> Rebuild and open in dev container.

### Interactive terminal:
- `./enter_dev_container.sh` (Unix) or `./enter_dev_container.bat` (Windows):
    - This builds and enters the container through an interactive terminal, while forwarding the ports needed by the application.
    - Upon leaving the terminal, this automatically deletes the container.

This dev container should automatically install all front-end and back-end dependencies and provide a standard development environment.

(Once in full dev container view or interactive terminal)
#### Building front-end:
1. Navigate to the `frontend` directory.
2. Run `npm install`:
    - Updates front-end dependencies. This is run automatically upon entering the container but needs to be re-run if dependencies change mid-session.
3. Run `npm run build`:
    - The web page only works as intended if the front-end has been built since the last changes.

#### Executing back-end:
1. Navigate to the `backend` directory.
2. Run `python3 main.py`:
    - Serves the built web page and interfaces with APIs.
Alternatively, run `./start_server.sh` to automate the build/execute process.
```
