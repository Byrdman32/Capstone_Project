# Development Workflow

Follow the steps below to set up your environment, build the front-end, and run the back-end server with Swagger UI support.

---

## API Token Setup (optional)

1. Retrieve the API token from the Discord server.
2. Save the token to:

   ```
   backend/backend_modules/tokens/api_token
   ```

---

## Dev Container Usage

You can either use **VS Code Dev Container View** or run an **interactive terminal** for development.

### Option 1: Open in VS Code (Recommended)

1. Press `Ctrl + Shift + P`
2. Select: **Dev Containers: Rebuild and Reopen in Container**

### Option 2: Interactive Terminal

1. From the project root, run:

   ```
   ./enter_dev_container.sh        # For Unix
   ./enter_dev_container.bat       # For Windows
   ```

2. This will:

   * Build the container
   * Forward required ports
   * Install all dependencies
   * Automatically clean up on exit

---

## Building the Front-End

1. Navigate to the front-end directory:

   ```
   cd frontend
   ```

2. Install dependencies (re-run if `package.json` changes):

   ```
   npm install
   ```

3. Build the front-end:

   ```
   npm run build
   ```

---

## Running the Back-End

### Option 1: Manual Start

1. Navigate to the back-end:

   ```
   cd backend
   ```

2. Run the server:

   ```
   python3 -m backend.main
   ```

### Option 2: Automated Script

From the project root:

```
./start_server.sh
```

> This will build the front-end and start the back-end server in one step.

---

## Swagger UI

Once the server is running, access the auto-generated Swagger documentation at:

```
http://localhost:9000/swagger
```

> Use Swagger to explore and test the API endpoints directly from the browser.