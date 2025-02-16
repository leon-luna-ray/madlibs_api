import axios from 'axios';

import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useGameStore = defineStore('game', () => {
    const isActive = ref(false);
    const isLoading = ref(false);
    const storyData = ref(null);
    const userResponses = ref([]);

    const fetchRandomStory = async () => {
        isLoading.value = true;

        try {
            const response = await axios.get('/random');
            console.log(response.data);

            storyData.value = response.data;
        } catch (error) {
            console.error('Error fetching random story:', error);
        } finally {
            isLoading.value = false;
        }
    }

    const start = () => {
        isActive.value = true;
        fetchRandomStory();
    }

    return {
        isActive,
        isLoading,
        storyData,
        userResponses,
        fetchRandomStory,
        start,
    }
});
