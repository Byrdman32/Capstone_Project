# npm run dev starts an interactive server that will hot-reload modules, changing them immediately as they are edited

npm --prefix ./frontend install
python3 -m backend.main --refreshdb
npm --prefix ./frontend run dev