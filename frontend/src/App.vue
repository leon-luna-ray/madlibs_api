<template>
  <div class="flex flex-col min-h-screen">
    <Header />
    <RouterView class="flex-grow" />
    <Footer />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterView } from 'vue-router'
import { useUiStore } from './stores/ui';

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const ui = useUiStore();

onMounted(() => {
  ui.setFontsLoaded();
  ui.setReduceMotion();
});
</script>
