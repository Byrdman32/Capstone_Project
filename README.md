# Development Workflow

To get started, follow the steps below to set up the environment, build the front-end, and run the back-end.

---

## API Token Setup

1. Retrieve the API token from the Discord server.
2. Save the token to the following file path:

(Once in full dev container view or interactive terminal)
Run `./start_dev.sh` (live changes) or `./start_server.sh` (builds then serves) to start the front-end and back-end servers
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

(Once in full dev container view or interactive terminal)

1. Navigate to the `root` directory of the project and run:
   ```
   ./start_server.sh
   ```
   or
   ```
   ./start_dev.sh
   ```

   This script builds the front-end and starts the back-end in one step.