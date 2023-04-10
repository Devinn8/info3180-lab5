<script setup>
import { ref, onMounted } from 'vue'
import MovieForm from "@/components/MovieForm.vue";
let movies = ref([])

onMounted(() => {
    fetch("/api/v1/movies")
    .then((resp) => resp.json())
    .then((data) => {
        movies.value = data.movies;
    })
    .catch((err) => console.log(err));
})
const update = (e) => {
    movies.value = e;
};
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