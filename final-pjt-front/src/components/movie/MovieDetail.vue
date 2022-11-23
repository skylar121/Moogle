<template>
  <div class="container">
    <h2 class="card-title my-3">{{ movie?.title }}</h2>
    <h5 v-if="movie?.tagline">
      <i class="fa-solid fa-quote-left"></i>
      <span> {{ movie?.tagline }} </span>
      <i class="fa-solid fa-quote-right"></i> </h5>
    <p class="card-text my-3 text-muted">{{ movie?.overview }} </p>
    
    <div class="additional-details">
      <div class="row">
        <div class="col">
          <h6>장르</h6>
          <p class="mt-3 mb-4"><span class="genre-list" v-for="genre in movie?.genres" :key="genre['id']">{{ genre['name'] }}</span></p>
          <!-- {{ genres_list.filter(genreId => genre['id'] === genreId) }} -->
        </div>
      </div>
      <div class="row">
        <div class="col">
          <h6>평균 별점</h6>
          <div v-if="movieVoteAverage" class="movieVoteAverage">
            <b-form-rating
              v-model="movieVoteAverage"
              readonly
              show-value
              show-value-max
              precision="1"
              color="#ffd21e"
              class="border-0 text-light"
              size="lg"
            ></b-form-rating>
            <!-- <p>{{ movie?.vote_average.toFixed(1) > 0.0 ? `⭐${movie?.vote_average.toFixed(1)} / 10` : '아직 별점이 없어요!' }} </p> -->
          </div>
          <p v-else>아직 별점이 없어요!</p>
        </div>
        <div class="col">
          <h6>개봉일</h6>
          <p>{{ movie?.release_date }}</p>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <h6>감독</h6>
          <a :href="`https://www.themoviedb.org/person/${director?.id}`">{{ director?.name }}</a>
        </div>
        <div class="col">
          <h6>배우</h6>
          <a v-for="actor in cast" :key="actor?.id" :href="`https://www.themoviedb.org/person/${actor?.id}`">
            <img v-if="actor?.profile_path" class="rounded-circle actor-img m-2" height="60" width ="60" :src="'https://image.tmdb.org/t/p/original' + actor?.profile_path" alt="">
          </a>
        </div>
      </div>
    </div>
    <!-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> -->
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  props: {
    movie: Object,
    cast: Array,
    director: Object,
  },
  data() {
    return {
      movieVoteAverage: null, 
      // movie_genres(genres_list) {
      //   genres_list.filter(genreItem => genreItem['id'] === genreId)
      // }
    }
  },
  computed: {
    ...mapState([
      'genres_list',
    ]),
    // thisMovieGenres() {
    //   const genres_list =  this.$store.state.genres_list
    //   return genres_list.filter(genre => genre['id'] === genreId)
    // },
  },
  created() {
    this.movieVoteAverage = this.movie.vote_average.toFixed(1) > 0.0 ? (this.movie.vote_average / 2).toFixed(1) : null
  },
}
</script>

<style lang="scss">
.card {
  background: $body-bg;
  border: none;
  .card-title {
    font-size: 2.7rem;
    font-weight: 800;
  }
  .card-text {
    /* word-break: keep-all; */
  }
  a {
    color: white;
  }
  h6 {
    color: $primary;
    font-weight: 600;
    font-size: 1.1rem;
  }
  .genre .additional-details {
    font-size: 1.5em;
  }
}

.movieVoteAverage {
  width: 80%;
}

.genre-list {
  background-color: $primary;
  border-radius: $borderRadius;
  padding: .3em .7em;
  margin-right: .5em;
  text-align: center;
  /* font-weight: 600; */
}

.actor-img {
  object-fit: cover;
  margin-right: .5em;
}

</style>