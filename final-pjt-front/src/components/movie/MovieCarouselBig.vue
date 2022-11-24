<template>
  <carousel-3d
    v-if="recommendMovies"
    :controls-visible="true"
    :inverse-scaling="200"
    :disable3d="false"
    :space="400" :display="9"
    :height="600"
    autoplay
  >
    <slide 
      v-for="(movie, idx) in recommendMovies" 
      :key="movie.id" 
      :index="idx" 
      @click="routeDetail(movie.id)"
    >
      <template slot-scope="{ index }" >
        <div 
          @click.stop="routeDetail(movie.id)" 
          class="movie-item" 
          :data-index="index"
        >
          <img 
            :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" :height="500"
          >
          <div class="movie-item-info">
            <ul>
              <div>
                <li>
                  <button v-if="!isLiked" @click.stop="toggleMovieLike(currUser.id, movie.id)" style="z-index: 3;"><span span id="movie-detail-like" style="color: #dd3c3c;"><i class="fa-regular fa-heart me-2 fs-1"></i></span></button>
                  <button v-else @click.stop="toggleMovieLike(currUser.id, movie.id)" style="color: #dd3c3c; z-index: 3;"><span span id="movie-detail-like" style="color: #e64949;"><i class="fa-solid fa-heart me-2 fs-1"></i></span></button>
                </li>
              </div>
            </ul>
          </div>
          <div class="movie-swipe-big">
            <div class="movie-title-big">{{ movie.title }} </div>
            <div class="movie-rating-big">예상별점 ⭐{{ (movie?.vote_average/2).toFixed(1) }}</div>
          </div>
        </div>
      </template>
    </slide>
  </carousel-3d>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { Carousel3d, Slide } from 'vue-carousel-3d'
import axios from 'axios'
import api from '@/api/api'

export default {
  name: 'MovieCarouselBig',
  components: {
    Carousel3d,
    Slide,
  },
  data() {
    return {
      isLiked: null,
    }
  },
  computed: {
    ...mapState([
      'recommendMovies',
      'token',
      'currUser',
    ]),
  },
  methods: {
    ...mapActions([
      'fetchRecommendMovies',
    ]),
    routeDetail(id) {
      // console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: id }})
    },
    toggleMovieLike(userId, movieId) {
      console.log(userId, movieId)
      axios({
        method: 'get',
        url: api.movies.toggleMovieLike(this.currUser.id, this.$route.params.movie_id),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          this.isLiked = res.data
          console.log(this.isLiked)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.fetchRecommendMovies()
  }
}
</script>

<style>
.movie-item {
  position: relative;
}

.movie-item:hover .movie-item-info,
.movie-item:focus .movie-item-info {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.3);
}

.movie-item-info {
    display: none;
}
</style>