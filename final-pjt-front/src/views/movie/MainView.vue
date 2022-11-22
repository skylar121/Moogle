<template>
  <div>
    <section class="display">
      <div v-if="currUser" class="row-title">
        <span class="text-primary">{{ currUser.username }}</span>
        님을 위해 준비했어요!
      </div>
      <div v-else class="row-title">
        <span class="text-primary">추천 영화 <span class="text-muted fs-6"> 나만을 위한 추천을 보고싶다면 로그인!</span></span>
      </div>
      <MovieCarouselBig />
    </section>
    
    <section class="display">
      <div class="row-title">
        현재 상영중인 영화
      </div>
      <MovieCarouselSmall :movie-data="shuffledNowPlayingMovies" />

      <div class="row-title">
        영화도 나는 멜로
      </div>
      <MovieCarouselSmall :movie-data="romanceMovies" />

      <div class="row-title">
        너는 액션<span class="text-muted fs-6"> 난 피자 너는 순두부</span>
      </div>
      <MovieCarouselSmall :movie-data="actionMovies" />

    </section>
  </div>

</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'

import MovieCarouselBig from '@/components/movie/MovieCarouselBig'
import MovieCarouselSmall from '@/components/movie/MovieCarouselSmall'

export default {
  name: 'MainView',
  components: {
    MovieCarouselBig,
    MovieCarouselSmall,
  },
  computed: {
    ...mapState([
      'currUser',
      'actionMovies',
      'romanceMovies',
    ]),
    ...mapGetters([
      'shuffledNowPlayingMovies',
    ]),
  },
  methods: {
    ...mapActions([
      'fetchRecommendMovies',
      'fetchNowPlayingMovies',
      'fetchActionMovies',
      'fetchRomanceMovies',
    ]),
  },
  created() {
    this.fetchRecommendMovies()
    this.fetchNowPlayingMovies()
    this.fetchActionMovies()
    this.fetchRomanceMovies()
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
      /* width: 70%; */
      /* left: 50%; */
      /* bottom: -0.3em; */
      /* transform: translate(-50%, -50%); */
      /* border-radius: 10px; */
      width: 80%;
      left: 10%;
      bottom: 0;
      backdrop-filter: blur(8px);
      border-bottom: 2px solid $primary;
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