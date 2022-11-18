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
        <div @click="routeDetail(movie.id)" class="movie-item" :data-index="index">
          <img :src="'https://image.tmdb.org/t/p/original' + movie.backdrop_path" :height="180">
          <div class="movie-swipe-small">
            <span class="movie-title-small">{{ movie.title }}</span>
            <span>{{ movie?.vote_average.toFixed(1) > 0.0 ? `⭐${movie?.vote_average.toFixed(1)}` : '' }}</span>
          </div>
        </div>
      </template>
    </slide>
  </carousel-3d>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'MovieListCarouselSmall',
  components: {
    Carousel3d,
    Slide,
  },
  props: {
    movieData: Array,
  },
  methods: {
    routeDetail(id) {
      // console.log('클릭', tmdb_id)
      this.$router.push({ name: 'DetailView', params: { movie_id: id }})
    }
  },
}
</script>

<style>

</style>