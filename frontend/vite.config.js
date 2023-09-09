// vite.config.js
export default {
  build: {
    outDir: '../madlibs_api/static/dist',
    rollupOptions: {
      output: {
        entryFileNames: 'index.js',
        assetFileNames: 'index.css',
      },
    },
  },
};
