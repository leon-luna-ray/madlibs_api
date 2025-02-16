import { computed } from 'vue';
import { defineStore } from 'pinia';

export const useUiStore = defineStore('ui', () => {
    // State
    const reduceMotion = computed(() => {
        return document.body.classList.contains('reduce-motion')
    })

    // Methods
    const setFontsLoaded = async () => {
        await document.fonts.ready
        document.body.classList.add('fonts-loaded')
    }

    const setReducedMotion = () => {
        if (window.matchMedia('(prefers-reduced-motion)').matches) {
            document.body.classList.add('reduce-motion')
        }
    }

    return {
        reduceMotion,
        setFontsLoaded,
        setReducedMotion,
    }
});