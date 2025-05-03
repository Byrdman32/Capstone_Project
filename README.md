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
Run `./start_dev.sh` (live changes) or `./start_server.sh` (builds then serves) to start the front-end and back-end servers
```
