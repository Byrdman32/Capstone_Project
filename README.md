# Project Overview

This is a full-stack web application featuring a **React** front-end and a **Flask** back-end API. It includes:

* **Interactive API documentation and testing** via Swagger UI
* **React-based user interface** built with modern JavaScript tooling
* **Dev Container support** for seamless, portable development environments using Docker
* **PyTest-based testing suite** with optional code coverage reporting

---

# Setup Instructions

### Prerequisites

* [Docker](https://www.docker.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Dev Containers VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

---

# Development Workflow

Follow these steps to set up, build, and run both front-end and back-end services.

---

## Dev Container Usage

### Option 1: VS Code Dev Container (Recommended)

1. Open VS Code
2. Press `Ctrl + Shift + P`
3. Select: **Dev Containers: Rebuild and Reopen in Container**

### Option 2: Interactive Terminal

From the project root:

```bash
./enter_dev_container.sh        # Unix
./enter_dev_container.bat       # Windows
```

This script:

* Builds the container
* Forwards required ports
* Installs dependencies
* Cleans up automatically on exit

---

## Building the Front-End (React)

1. Navigate to the front-end directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Build the React application:

   ```bash
   npm run build
   ```

> Re-run `npm install` if `package.json` changes.

---

## Running the Back-End (Flask)

### Option 1: Manual Start

```bash
cd backend
python3 -m backend.main
```

### Option 2: Unified Script

```bash
./start_server.sh
```

This script:

* Builds the front-end
* Launches the back-end server

---

## Swagger UI

Once the server is running, visit:

```
http://localhost:9000/swagger
```

Use Swagger UI to:

* Explore API endpoints
* Test input/output formats
* View validation and error responses

---

## Unit Tests & Code Coverage

### Run All Unit Tests

```bash
PYTHONPATH=. pytest -p no:warnings -v
```

### Run Tests with Coverage

```bash
PYTHONPATH=. pytest --cov=backend -p no:warnings --cov-config=.coveragerc -v
```

### Generate HTML Coverage Report

```bash
PYTHONPATH=. pytest --cov=backend --cov-report=html --cov-config=.coveragerc -p no:warnings -v
```

> Tests are located in `backend/tests/` and follow `pytest` standards.

---

# Team Contributions

This project was made possible by the collaborative efforts of the following team members:

* **Viktor Butkovich** ([@Viktor-Butkovich](https://github.com/Viktor-Butkovich)) - *Front-end development*
* **Eli Byrd** ([@byrdman32](https://github.com/byrdman32)) - *Back-end API Development*
* **Kevin Mccole** ([@Stickydarp](https://github.com/Stickydarp)) - *Testing and AI integration*
* **Duncan Truitt** ([@copper-head](https://github.com/copper-head)) - *Backend API/Database development*
* **Melesio Albavera** ([@me11203sci](https://github.com/me11203sci))
