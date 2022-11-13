<template>
  <div class="container">
    <h3 class="m-3">오늘의 추천 영화</h3>
    <div class="card m-5" style="width: 18rem;">
      <img :src="'https://image.tmdb.org/t/p/w300'+movieData[randomNumber].poster_path" class="card-img-top" alt="" height="400px">
      <div class="card-body">
        <h5 class="card-title">{{ movieData[randomNumber].title }}</h5>
        <p class="card-text">{{movieData[randomNumber].overview.substr(0, 100)}}...</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RandomView',
  computed: {
    movieData() {
      return this.$store.state.movieData
    },
    randomNumber() {
      return Math.floor(Math.random()*20)
    }

  },
  created() {
    if (this.$store.state.movieData === null) {
      this.$store.dispatch('fetchMovie')
    }
  },
}
</script>

<style>

</style>