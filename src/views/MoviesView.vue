<template>

    <div class="main-container">
        <h1 class="page-header">Movies</h1>
        <div class = "container">
        <div v-for="(movie, index) in movies" :key="index" class="card">
            <div class="card-body">
            <div class="row">
                <div class="col-md-4">
                <img :src="movie.poster" class="card-img-top" alt="Movie Poster">
                </div>
                <div class="col-md-8">
                <h5 class="card-title">{{ movie.title }}</h5>
                <p class="card-text">{{ movie.description }}</p>
                </div>
            </div>
            </div>
        </div>
        </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  let movies = ref([]);
  
  function fetchMovies() {
    fetch("/api/v1/movies")
      .then(response => {
        if (!response.ok) {
          throw new Error("Failed to fetch movies");
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
        movies.value = data.movies;
      })
      .catch(error => {
        console.error("Error fetching movies:", error);
      });
  }
  
  onMounted(() => {
    fetchMovies();
  });
  </script>

<style>

.container{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 100%;
    gap: 20px;
}
.card{
    height: 250px;
    width: 500px;
    margin-right: 40px;
}

.card-body{
    padding: 0px;
}

.card-body img{
    height: 100%;
    padding: 2%;
}

.row{
    margin-left:0px;
}

.row .col-md-8{
    padding: 20px;
    padding-right: 27px;
}

.row .col-md-4{
    padding: 0px;
}

.main-container h1 {
    margin-left:70px;
    margin-bottom:15px;
}

</style>

