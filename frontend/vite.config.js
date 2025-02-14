// vite.config.js
export default {
  build: {
    outDir: '../backend/madlibs_ai/static/dist',
    rollupOptions: {
      output: {
        entryFileNames: 'index.js',
        assetFileNames: 'index.css',
      },
    },
  },
};
