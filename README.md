workflow:

Setup:
React does not start out with the node_modules folder, which contains all of its dependencies.
    To install these dependencies, run "npm install" in the directory - this installs all the dependencies it finds in package.json
    These dependencies are too large to include directly in the repository
To set up the API token, get our API token from the Discord server, then put copy it to a file called api_token (no file handle)

To run back-end server:
npm run build
    If this doesn't work, install any dependencies like "npm install axios"
    Running this creates new static files in the build folder
    You may also need to set up npm itself
py backend.py
    Running this starts the server and backend API, which serves the static files from the build folder
Follow URL to open the app in a web browser
    Refresh the page to re-render and update any content from the back-end (like the timer)

To access exoplanet API:
Run main.py
    The # %% lines denote Jupytext cells, which allows running like a Jupyter notebook or as a normal Python script
