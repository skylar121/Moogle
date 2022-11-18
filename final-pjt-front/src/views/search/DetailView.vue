<template>
  <div>
    <section class="section">
      <img class="section-left" :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="" width="300">
      <div class="section-right">
        <h1>{{ movie.title }}</h1>
        <form @submit.prevent="createReview" class="form">
        </form>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
const MOVIE_URL = 'https://api.themoviedb.org/3/movie'
// const API_URL = 'http://127.0.0.1:8000/movies'

export default {
  name: 'DetailView',
  data() {
    return {
      movie: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${MOVIE_URL}/${this.$route.params.id}`,
        params: {
          api_key: process.env.VUE_APP_TMDB,
          language: 'ko-KR',
        },
      })
      // axios({
      //   method: 'get',
      //   url: `${API_URL}/${this.$route.params.movie_id}/`,
      //   // params: {
      //   //   api_key: process.env.VUE_APP_TMDB,
      //   //   language: 'ko-KR',
      //   // },
      // })
        .then((res) => {
          this.movie = res.data
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style lang="scss">
.section {
  width: 80%;
  height: 600px;
  background-color: white;
  color: black;
  margin: 5em auto;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  flex: 20%;
}

.section-left {
  flex-basis: 40%;
  height: 100%;
  overflow: hidden;
  /* object-fit: none; Do not scale the image */
  /* object-position: center; Center the image within the element */
}

.section-right {
  height: 100%;
  flex-basis: 60%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  margin: 0 auto;
  
}
.section-right h1 {
  margin: 1em auto;
}

.section-right form {
  width: 50%;
  margin: 3em auto;
  text-align: left;
}

.section-right form input {
  width: 100%;
  border-bottom: 1px solid #BF93FF;
  outline: none;
  margin-bottom: 1.2em;
}

.link {
  display: block;
  text-align:center;
  font-size: .8rem;
  margin-top: -.8em;
}

// .link:hover {
//   color: orange;
// }

</style>