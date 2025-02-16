// import axios from 'axios';
import { defineStore } from 'pinia';

export const useGameStore = defineStore('game', () => {
    const data = ref(null);

    // const fetchRandomStory = async () => {
    //     const response = await axios.get('/api/game/random');
    //     data.value = response.data;
    // }

    return {
        data,
    }
});