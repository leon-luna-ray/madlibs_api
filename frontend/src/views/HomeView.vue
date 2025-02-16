<template>
  <div class="container flex items-center justify-center h-full h-full flex-grow">
    <transition name="fade" mode="out-in">
      <section v-if="game.isActive" class="h-full">
        <InputPanel v-if="game.storyData" :data="game.storyData.blanks" />
      </section>
      <section v-else class="flex-col-2 items-center">
        <div class="text-center">
          <p>Welcome to Madlibs AI! This is a simple game where you can create your own madlib stories.</p>
          <p>Click the button below to start a new game.</p>
        </div>
        <button @click="game.start" class="btn w-max">Start New Game</button>
      </section>
    </transition>
  </div>
</template>

<script setup>
import { useGameStore } from '@/stores/game';

import InputPanel from '@/components/InputPanel.vue';

const game = useGameStore();
</script>
