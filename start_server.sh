# npm run preview starts a static server that serves the built/compiled files

npm --prefix ./frontend install
python3 -m backend.main --refreshdb
npm --prefix ./frontend run build
npm --prefix ./frontend run preview