<template>
    <footer>
        <div class="container text-center flex justify-center py-[1.5rem] opacity-50">
            <p class="body-text-3 uppercase">&copy; <a href="https://www.rayluna.dev" target="_blank" class="underline">rayluna.dev</a> {{ year }}</p>
        </div>
    </footer>
</template>

<script setup>
const year = new Date().getFullYear();
</script>
