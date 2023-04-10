<script setup>

import MovieForm from "@/components/MovieForm.vue";

</script>

<template>
    <main class="container py-5">
        <h1 class="display-1 mb-3">Add a Movie</h1>
        <MovieForm :movies="movies" @add-item="update" />
        <ul>
            <li v-for="movie in movies" :key="movie.id">{{ movie.title }}</li>
        </ul>
    </main>
</template>