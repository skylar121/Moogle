<template>
  <div class="card-body p-4">
    <h2 class="card-title my-3">{{ movie?.title }}</h2>
    <h5 v-if="movie?.tagline">{{ movie?.tagline }}</h5>
    <p class="card-text my-3">{{ movie?.overview }}</p>
    <!-- 장르 -->
    <div class="col mb-3 mt-3 genre">
      <h6>장르</h6>
      <span class="genre-list" v-for="genre in movie?.genres" :key="genre['id']">{{ genre['name'] }}</span>
    </div>
    <!-- 디테일 -->
    <div class="additional-details">
      <div class="row">
        <div class="col">
          <h6>개봉일</h6>
          <p>{{ movie?.release_date }}</p>
        </div>
        <div class="col">
          <h6>평균 별점</h6>
          <p>{{ movie?.vote_average.toFixed(1) > 0.0 ? `⭐${movie?.vote_average.toFixed(1)} / 10` : '아직 별점이 없어요!' }} </p>
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
            <img v-if="actor?.profile_path" class="rounded-circle actor-img" height="70" width ="70" :src="'https://image.tmdb.org/t/p/original' + actor?.profile_path" alt="">
          </a>
        </div>
      </div>
    </div>
    <!-- <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> -->
  </div>
</template>

<script>
export default {
  name: 'MovieItemDetail',
  props: {
    movie: Object,
    cast: Array,
    director: Object,
  }
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
  a {
    color: white;
  }
  h6 {
    color: $primary;
  }
  .genre .additional-details {
    font-size: 1.5em;
  }
}

.genre-list {
  background-color: $primary;
  border-radius: $borderRadius;
  padding: .3em;
  margin-right: .5em;
  text-align: center;
}

.actor-img {
  object-fit: cover;
  margin-right: .5em;
}

</style>