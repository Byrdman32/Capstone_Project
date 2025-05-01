import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: { // Ensure server can access file system changes for hot-module replacement, even in a Docker container
    watch: {
      usePolling: true,
    },
    port: 5173,
    host: '0.0.0.0',
    proxy: {
      '/api': {
        target: 'http://localhost:9000',
        changeOrigin: true,
      }
    }
  },
  preview: {
    port: 5173,
  }
})
