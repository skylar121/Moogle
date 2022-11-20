<template>
  <div class="container mt-4">
    <h6>비슷한 영화 추천</h6>
    <carousel-3d
      v-if="similarMovies"
      :controls-visible="true"
      :inverse-scaling="200"
      :disable3d="true"
      :space="230" :display="9"
      :width="210"
      :height="330"
    >
      <slide
        v-for="(movie, idx) in similarMovies"
        :key="movie.id"
        :index="idx"
        @click="routeDetail(movie.id)"
      >
        <template slot-scope="{ index }" >
          <div @click="routeDetail(movie.id)" class="movie-item" :data-index="index">
            <img :src="movie.poster_path ? 'https://image.tmdb.org/t/p/original' + movie.poster_path : 'https://image.tmdb.org/t/p/original' + movie.backdrop_path" :height="300">
            <!-- <div class="movie-swipe-big">
              <div class="movie-title-big">{{ movie.title }} </div>
              <div class="movie-rating-big">예상별점 ⭐{{ (movie?.vote_average/2).toFixed(1) }}</div>
            </div> -->
          </div>
        </template>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d'
export default {
  name: 'MovieSimilar',
  components: {
    Carousel3d,
    Slide,
  },
  data() {
    return {
      similarMovies: null,
    }
  },
  created() {
    this.fetchSimilarMovies()
  },
  methods: {
    fetchSimilarMovies() {
      const MOVIE_URL = 'https://api.themoviedb.org/3/movie'
      axios({
        method: 'get',
        url: `${MOVIE_URL}/${this.$route.params.movie_id}/similar`,
        params: {
          api_key: process.env.VUE_APP_TMDB,
          language: 'ko-KR',
        },
      })
        .then((res) => {
          // console.log(res)
          // 지금 보고 있는 영화는 제외하고 추천
          this.similarMovies = res.data.results.filter(movie => movie.id !== this.$route.params.movie_id)
          // console.log(this.similarMovies)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    routeDetail(id) {
      this.$router.replace({ name: 'DetailView', params: { movie_id: id }}).catch(()=>{})
      this.$router.go()
    },
  },
}
</script>

<style>

</style>