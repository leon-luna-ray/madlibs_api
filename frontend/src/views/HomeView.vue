<template>
  <main>
    <div class="container">
      <div class="flex-col-05">

        <p>Welcome to Madlibs AI! This is a simple game where you can create your own madlib stories.</p>
        <p>Click the button below to start a new game.</p>
        <button @click="game.fetchRandomStory" class="btn w-max">Start New Game</button>
      </div>
    </div>
  </main>
</template>

<script setup>
import { useGameStore } from '@/stores/game';

const game = useGameStore();
</script>