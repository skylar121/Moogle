<template>
  <carousel-3d
    v-if="shuffledRecommendMovies"
    :controls-visible="true"
    :inverse-scaling="200"
    :disable3d="false"
    :space="400" :display="9"
    :height="600"
    autoplay
  >
    <slide 
      v-for="(movie, idx) in shuffledRecommendMovies" 
      :key="movie.id" 
      :index="idx" 
      @click="routeDetail(movie.id)"
    >
      <template slot-scope="{ index }" >
        <div @click="routeDetail(movie.id)" class="movie-item" :data-index="index">
          <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" :height="500">
          <div class="movie-swipe-big">
            <div class="movie-title-big">{{ movie.title }} </div>
            <div class="movie-rating-big">예상별점 ⭐{{ movie.vote_average }}</div>
          </div>
        </div>
      </template>
    </slide>
  </carousel-3d>
</template>

<script>
import { mapGetters } from 'vuex'
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'MovieListCarouselBig',
  components: {
    Carousel3d,
    Slide,
  },
  computed: {
    ...mapGetters([
      'shuffledRecommendMovies',
    ]),
  },
  methods: {
    routeDetail(id) {
      // console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: id }})
    }
  },
}
</script>
