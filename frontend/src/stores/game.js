import axios from 'axios';

import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useGameStore = defineStore('game', () => {
    const storyData = ref(null);

    const fetchRandomStory = async () => {
        const response = await axios.get('/random');

        console.log(response.data);
        storyData.value = response.data;
    }

    return {
        storyData,
        fetchRandomStory,
    }
});