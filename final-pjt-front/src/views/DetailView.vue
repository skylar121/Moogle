<template>
  <div>
    <p>뜨냐,,?</p>
    <!-- <section class="section"> -->
      <!-- <img class="section-left" :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" alt="" width="300"> -->
      <!-- <div class="section-right">
        <h1>{{ movie.title }}</h1>
        <form @submit.prevent="signUp" class="form">
          <label for="username">아이디 </label><br>
          <input type="text" id="username" v-model="username" required>
          <br>
          <label for="password1"> 비밀번호 </label><br>
          <input type="password" id="password1" v-model="password1" required minlength="8">
          <br>
          <label for="password2"> 비밀번호 확인 </label><br>
          <input type="password" id="password2" v-model="password2" required minlength="8">
          <br>
          <input type="submit" value="회원가입"  class="btn btn-primary">
          <router-link :to="{ name: 'LogInView' }" class="link">이미 회원이신가요? 로그인하기</router-link>
        </form>
      </div>
    </section> -->
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
  object-fit: none; /* Do not scale the image */
  object-position: center; /* Center the image within the element */
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