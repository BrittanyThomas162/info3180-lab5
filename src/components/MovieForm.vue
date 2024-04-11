<template>
    <div>
       <div v-if="displayFlash" class="alert" :class="{ 'alert-success': isSuccess, 'alert-danger': !isSuccess }">
         {{ flashMessage }}
       </div>
       <form @submit.prevent="saveMovie" id="movieForm">
         <div class="form-group mb-3">
           <label for="title" class="form-label">Movie Title</label>
           <input type="text" id="title" v-model="title" name="title" class="form-control" />
         </div>
   
         <div class="form-group mb-3">
           <label for="description" class="form-label">Movie Description</label>
           <textarea id="description" v-model="description" name="description" class="form-control"></textarea>
         </div>
   
         <div class="form-group mb-3">
           <label for="poster" class="form-label">Movie Poster</label>
           <input type="file" id="poster" @change="onFileChange" name="poster" class="form-control" accept=".jpg,.png" />
         </div>
   
         <input type="submit" value="Submit">
       </form>
    </div>
</template>
   
  
<script setup>

    import { ref, onMounted } from "vue";   
    
    let csrf_token = ref("");

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
    

    function saveMovie() {

        let movieForm = document.getElementById('movieForm');    
        let form_data = new FormData(movieForm)

        fetch("/api/v1/movies", {
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
      
    }

</script>

