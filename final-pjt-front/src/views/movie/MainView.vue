<template>
  <div>
    <section class="display">
      <div class="row-title">
        {{ userNickname }} 님을 위한 추천
      </div>
      <MovieListCarouselBig />
    </section>
    
    <section class="display">
      <div class="row-title">
        현재 상영중인 영화
      </div>
      <MovieListCarouselSmall :movieData="nowPlayingMovies" />

      <div class="row-title">
        Actions
      </div>
      <MovieListCarouselSmall :movieData="actionMovies" />

      <!-- 3. 장르별 영화 -->
      <div class="row-title">
        Romance
      </div>
      <MovieListCarouselSmall :movieData="nowPlayingMovies" />
    </section>
  </div>

</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

import MovieListCarouselBig from '@/components/movie/MovieListCarouselBig'
import MovieListCarouselSmall from '@/components/movie/MovieListCarouselSmall'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MainView',
  components: {
    MovieListCarouselBig,
    MovieListCarouselSmall,
  },
  data() {
    return {
      videoUrl: null,
      isHovered: false,
      nowPlayingMovies: null,
      actionMovies: null,
      romanceMovies: null,
    }
  },
  methods: {
    getNowPlayingMovies() {
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
          // console.log('상영중', response.data.results)
          this.nowPlayingMovies = this.shuffle(response.data.results)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getActionMovies() {
      axios.get(API_URL + '/movies/action10')
        .then((response) => {
          // console.log(response.data)
          this.actionMovies = this.shuffle(response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    shuffle ([...arr]) {
      let m = arr.length;
      while (m) {
        const i = Math.floor(Math.random() * m--);
        [arr[m], arr[i]] = [arr[i], arr[m]];
      }
      return arr
    },
  },
  computed: {
    ...mapState([
      'userNickname',
      'isLogin',
    ]),
    // shuffleRecommendMovies() {
    //   return this.shuffle(this.recommendMovies)
    // },
  },
  created() {
    if (this.$store.state.recommendMovies === null) {
      this.$store.dispatch('fetchMovie')
    }
    this.getNowPlayingMovies()
    this.getActionMovies()
  },
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
      border: 2px solid $primary;
      text-align: center;
      text-decoration: none;
      min-height: 50px;
      display: flex;
      justify-content: center;
      align-items: center;
      white-space: nowrap;
      padding: .4em;
      overflow: hidden;
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
      white-space: nowrap;
      text-align: left;
      overflow: hidden;
      /* animation: textLoop 10s linear infinite; */
    }
  }
}

@keyframes textLoop {
  0% {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }
  100% {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
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