import { fileURLToPath, URL } from "node:url"
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";



// https://vitejs.dev/config/
export default defineConfig({
  base: "/",
  server: {
    host: '127.0.0.1'
  },
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  build: {
    outDir: "../madlibs_api/static/dist",
    rollupOptions: {
      output: {
        assetFileNames: (assetInfo) => {
          let extType = assetInfo.name.split('.').at(1);
          if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(extType)) {
            extType = 'img';
          }
          return `assets/${extType}/[name][extname]`;
        },
        chunkFileNames: 'assets/js/[name].js',
        entryFileNames: 'assets/js/[name].js',
      },
    },
    modulePreload: {
      resolveDependencies: () => [],
    },
  },
  experimental: {
    renderBuiltUrl(filename, hostId, hostType, type) {
        return '/static/dist/' + filename
    }
  }
});
