import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// vite.config.js
export default defineConfig({
  base: '/impersonator/',
  plugins: [svelte()]
});

