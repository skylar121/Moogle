<template>
  <div>
    <img class="background-img" :src="require(`@/assets/background.jpg`)" style="height: 100%; background-color: #000; opacity: 0.2;">
    <section class="display mt-3">
      <div v-if="currUser && userLikes && userLikes?.length > 0">
        <div class="row-title text-center fs-2 mb-5">
          <span class="text-primary">{{ currUser.nickname }}</span>
          님만을 위해 준비했어요!
        </div>
        <MovieCarouselBig />
      </div>
      <div v-else-if="!currUser && currUser === null">
        <div class="row-title text-center fs-2">
          <div class="text-primary">
            지금 인기있는 영화
            <p class="text-muted fs-6">당신만의 욕구셔테리어를 보고싶다면 로그인! 🐶</p>
          </div>
        </div>
        <MovieCarouselBig />
      </div>
      <div v-else-if="userLikes?.length < 1 " class="row-title text-center">
        <div class="text-primary fs-2">
          지금 인기있는 영화
          <div class="text-muted fs-6">더 자세한 추천을 위해 좋아요 남기러 갈까요?
          </div>
        </div>
        <MovieCarouselBig />
      </div>
    </section>
    
    <section class="display">
      <div class="row-title px-4">
        현재 상영중인 영화
      </div>
      <div v-if="shuffledNowPlayingMovies">

      <MovieCarouselSmall
      :movie-data="shuffledNowPlayingMovies" />
      </div>

      <div class="row-title px-4 mt-5">
        영화도 나는 멜로
      </div>
      <MovieCarouselSmall :movie-data="romanceMovies" />

      <div class="row-title px-4 mt-5">
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
      'userLikes',
      'recommendMovies',
      'actionMovies',
      'romanceMovies',
    ]),
    ...mapGetters([
      'shuffledNowPlayingMovies',
    ]),
    recommendLength() {
      return this?.shuffledNowPlayingMovies?.length
    }
  },
  methods: {
    ...mapActions([
      'getUserLikes',
      'getUserReviews',
      'fetchRecommendMovies',
      'fetchNowPlayingMovies',
      'fetchActionMovies',
      'fetchRomanceMovies',
      'calcUserRank',
    ]),
  },
  created() {
    this.fetchRecommendMovies()
    this.fetchNowPlayingMovies()
    this.fetchActionMovies()
    this.fetchRomanceMovies()
  },
  watch: {
    getUserLikes(){
      console.log(this.userLikes)
    }
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
      bottom: -4.5em;
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