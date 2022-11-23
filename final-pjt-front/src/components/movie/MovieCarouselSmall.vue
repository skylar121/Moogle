<template>
  <carousel-3d
    v-if="movieData"
    :controls-visible="true"
    :inverse-scaling="200"
    :disable3d="true"
    :space="360" :display="8"
    :height="200"
  >
    <slide 
      v-for="(movie, idx) in movieData" 
      :key="movie.id" 
      :index="idx" 
    >
      
      <template slot-scope="{ index }" >
        <div @click="goToDetail(movie.id)" class="movie-item" :data-index="index">
          <img :src="movie.backdrop_path ? 'https://image.tmdb.org/t/p/original' + movie.backdrop_path : 'https://image.tmdb.org/t/p/original' + movie.poster_path"  :height="180">
          <!-- <span id="ticket"><i class="fa-solid fa-ticket-simple fs-3"></i></span> -->
          <div class="movie-swipe-small">
            <span class="movie-title-small">{{ movie.title }}</span>
            <span>{{ (movie?.vote_average/2).toFixed(1) > 0.0 ? `⭐${(movie?.vote_average/2).toFixed(1)}` : '' }}</span>
          </div>
        </div>
      </template>
    </slide>
  </carousel-3d>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'MovieCarouselSmall',
  components: {
    Carousel3d,
    Slide,
  },
  props: {
    movieData: Array,
  },
  methods: {
    goToDetail(id) {
      // console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: id }})
    }
  },
}
</script>

<style>

</style>