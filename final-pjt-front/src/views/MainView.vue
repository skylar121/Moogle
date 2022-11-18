<template>
  <div>
    <!-- 마우스오버시 디테일 -->
    <div class="modal" :style="{ 'display': isHovered ? 'block' : 'none' }" @show-modal="showModal"
      @mouseleave="isHovered = false">
      <p>{{ videoUrl }}</p>
    </div>

    <section class="display">
      <!-- 1. 추천 인트로 -->
      <div class="row-title">
        {{ username }} 님을 위한 추천
      </div>
      <carousel-3d
        v-if="recommendMovies"
        :controls-visible="true"
        :inverse-scaling="200"
        :disable3d="false"
        :space="400" :display="9"
        :height="600"
        @mouseenter="showModal"
        autoplay
      >
        <slide v-for="(movie, idx) in recommendMovies" :key="movie.id" :index="idx">
          <!-- <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }"> -->
          <template slot-scope="{ index }" >
            <div class="movie-item" :data-index="index" @show-modal="showModal">
              <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
                <!-- <img  :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="'https://image.tmdb.org/t/p/original'+movie.poster_path" > -->
                <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" :height="500">
                <div class="movie-swipe-big">
                  <div class="movie-title-big">{{ movie.title }} </div>
                  <div class="movie-rating-big">예상별점 ⭐{{ movie.vote_average }}</div>
                </div>
              </router-link>
            </div>
          </template>
        </slide>
      </carousel-3d>
    </section>

    
    <section class="display">
      <!-- 2. 상영중인 영화 -->
      <div class="row-title">
        현재 상영중인 영화
      </div>
      <carousel-3d
        v-if="nowPlayingMovies"
        :controls-visible="true"
        :inverse-scaling="200"
        :disable3d="true"
        :space="360" :display="9"
        :height="200"
        @mouseenter="showModal"
        autoplay
      >
        <slide v-for="(movie, idx) in nowPlayingMovies" :key="movie.id" :index="idx">
          <template slot-scope="{ index }" >
            <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
              <div class="movie-item" :data-index="index" @show-modal="showModal">
                <img :src="'https://image.tmdb.org/t/p/original' + movie.backdrop_path" :height="180">
                <div class="movie-swipe-small">
                  <span class="movie-title-small">{{ movie.title }}</span>
                  <span>⭐{{ movie.vote_average }}</span>
                </div>
              </div>
            </router-link>
          </template>
        </slide>
      </carousel-3d>
      <!-- 3. 최신 영화 -->
    </section>
  </div>

</template>

<script>
import axios from 'axios'
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'MainView',
  components: {
    Carousel3d,
    Slide,
  },
  data() {
    return {
      videoUrl: null,
      isHovered: false,
      nowPlayingMovies: null,
    }
  },
  methods: {
    showModal(movie) {
      this.videoUrl = `https://www.youtube.com/results?search_query=${movie.title} 공식 예고편`
      this.isHovered = true
      console.log('카드 마우스오버');
    },
    fetchNowPlayingMovies() {
      const MOVIE_URL = 'https://api.themoviedb.org/3/movie/now_playing'
      axios.get(MOVIE_URL, {
        params: {
          api_key : process.env.VUE_APP_TMDB,
          language: 'ko-KR',
          page: 1,
          region: 'KR',
        }
      })
        .then((response) => {
          console.log(response.data.results)
          this.nowPlayingMovies = response.data.results
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  computed: {
    // 로그인시 username 가져오기 필요
    username() {
      return this.$store.state.username
    },
    recommendMovies() {
      return this.$store.state.recommendMovies
    },
  },
  created() {
    if (this.$store.state.recommendMovies === null) {
      this.$store.dispatch('fetchMovie')
    }
    this.fetchNowPlayingMovies()
  },
  mounted() {
  }
}
</script>

<style lang="scss">
.carousel-3d-container {

  .carousel-3d-slider {
    background: unset;
  }

  .carousel-3d-slide {
    background: unset;
    border: none;

    .movie-item {
      color: #fff;
      position: relative;
      cursor: pointer;
      transition: all 0.5s;
      -moz-transition: all 0.5s;
      -webkit-transition: all 0.5s;
      -o-transition: all 0.5s;
      text-decoration: none;
      :hover{
        color: $primary !important;
      }
    }
    
    .movie-swipe-big {
      position: absolute;
      width: 80%;
      left: 50%;
      bottom: -5.2em;
      transform: translate(-50%, -50%);
      text-align: center;
      text-decoration: none;
      :hover{
        color: $primary !important;
      }
    }
    

    .movie-swipe-small {
      position: absolute;
      width: 70%;
      left: 50%;
      bottom: -0.3em;
      transform: translate(-50%, -50%);
      backdrop-filter: blur(10px);
      border-radius: 10px;
      text-align: center;
      text-decoration: none;
      min-height: 50px;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .movie-title-big {
      font-size: 1.2rem;
      font-weight: 700;
    }

    .movie-rating-big {
      color: orange;
    }

    .movie-title-small {
      font-size: 1.02rem;
      font-weight: 700;
    }
  }
}

.row-title {
  font-size: 1.5rem;
  font-weight: 800;
}

.display {
  padding: 1em;
  /* height: 800px; */
  /* background-image: url('../assets/display.png') ; */
}

</style>