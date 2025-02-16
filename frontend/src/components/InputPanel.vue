<template>
    <section class="flex justify-center items-center h-full">
        <div v-if="inputs.length" class="flex-col-2 justify-cetner items-center lg:w-[75%]">
            <form class="p-[4rem] rounded-md text-center grid md:grid-cols-2 gap-[1rem]">
                <div class="form-input border p-[2rem]" v-for="(input, index) in inputs" :key="index">
                    <label class="h2">{{ inputs[index] }}</label>
                    <input type="text" v-model="userInput" class="text-[1.25rem] font-nunito" required />
                </div>
            </form>
            <button class="btn w-full uppercase text-center" @click="nextInput">Next</button>
        </div>
    </section>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useGameStore } from '@/stores/game';

const game = useGameStore();

const activeIndex = ref(0);
const userInput = ref('');

const inputs = computed(() => {
    return game.storyData?.blanks || [];
});

const nextInput = () => {
    const response = {
        type: inputs.value[activeIndex.value],
        value: userInput.value
    };

    game.userResponses.push(response);

    if (activeIndex.value < inputs.value.length - 1) {
        userInput.value = '';
        activeIndex.value++;
    } else {
        // game.submit();
    }
};
</script>
