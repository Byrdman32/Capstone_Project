# Development Workflow

To get started, follow the steps below to set up the environment, build the front-end, and run the back-end.

---

## API Token Setup

1. Retrieve the API token from the Discord server.
2. Save the token to the following file path:

   ```
   ./backend/backend_modules/tokens/api_token
   ```

---

## Using the Dev Container

You can work either in the full Dev Container view (recommended in VS Code) or via an interactive terminal.

### Option 1: Open in VS Code Dev Container

* Press `Ctrl + Shift + P`
* Select **Rebuild and Reopen in Container**

### Option 2: Use an Interactive Terminal

* Run the platform-specific script:

  * Unix: `./enter_dev_container.sh`
  * Windows: `./enter_dev_container.bat`
* This will:

  * Build and start the container with necessary port forwarding
  * Automatically remove the container upon exit

> The dev container automatically installs all front-end and back-end dependencies to ensure a consistent development environment.

---

## Building the Front-End

1. Navigate to the `frontend` directory:

   ```
   cd frontend
   ```
2. Install dependencies (automatically done at container startup, but re-run if `package.json` changes):

   ```
   npm install
   ```
3. Build the front-end:

   ```
   npm run build
   ```

---

## Running the Back-End

1. Navigate to the `backend` directory:

   ```
   cd backend
   ```
2. Run the server manually:

   ```
   python3 main.py
   ```

   OR
3. Use the automated script:

   ```
   ./start_server.sh
   ```

   This script builds the front-end and starts the back-end in one step.