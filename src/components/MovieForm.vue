<script setup>
import { ref, onMounted } from 'vue';
const props = defineProps(['movies'])
const emits = defineEmits(['add-item'])
let movie = ref("")
let csrf_token = ref("");
let message = ref("Successfully added!")


function getCsrfToken() {
 fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
 })
 }

 onMounted(() => {
 getCsrfToken();
    });

const saveMovie = () => {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    fetch('/api/v1/movies', {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        // display a success message
        console.log(data);
    })
    .catch(function (error) {
        console.log(error);
    });
};



</script>

<template>
<form method='POST' @submit.prevent="saveMovie" id="movieForm" >
    <div class="row">
        <div class="col-md-4">
            <div class="form-group mb-3">
                <label for="title" class="form-label">Movie Title</label>
                <input type="text" name="title" class="formcontrol" />
            </div>
            <div class="form-group mb-3">
                <label for="description" class="form-label">Movie Description</label>
                <textarea v-model="description" name="description" id="description" cols="30" rows="10" class="form-control"></textarea>
            </div>
            <div class="form-group mb-3">
                <div>
                    <label class="poster" for="image">Photo Upload</label>
                </div>
                
                <input type="file" class="formcontrol" name="poster" id="poster">
            </div>
            <div class="form-group mb-3">
                <button class="btn btn-primary" type="submit">Submit</button>
            </div>
        </div>
    </div>
</form>
</template>