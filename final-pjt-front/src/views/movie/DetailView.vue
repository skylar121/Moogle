<template>
  <div class="">
    <img class="background-img" :src="`https://image.tmdb.org/t/p/original${movie?.backdrop_path}`">
    <div class="container-lg mt-3">
      <div class="card mb-3">
        <div class="row g-0">
          <!-- 포스터 -->
          <div class="col-md-4">
            <img :src="'https://image.tmdb.org/t/p/original' + movie?.poster_path" class="img-fluid rounded-start" alt="">
          </div>
          <!-- 오른쪽 영역 -->
          <div class="col-md-8">
            <MovieItemReview :movie="movie" />
            <MovieItemDetail :movie="movie" :cast="cast" :director="director" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieItemReview from '@/components/movie/MovieItemReview'
import MovieItemDetail from '@/components/movie/MovieItemDetail'

const MOVIE_URL = 'https://api.themoviedb.org/3/movie'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    MovieItemReview,
    MovieItemDetail
  },
  data() {
    return {
      movie: null,
      cast: null,
      director: null,
    }
  },
  created() {
    console.log('라우팅 성공')
    this.getMovieDetail()
    this.getCredits()
  },
  methods: {
    getMovieDetail() {
      axios.get(API_URL + `/movies/${this.$route.params.movie_id}`)
      .then((res) => {
        console.log(this.$route.params.movie_id, res)
        // DB에 있다면 DB 정보 가져오기
        if (res['title'] !== undefined) {
          // console.log(res)
          this.movie = res
        } else {
        // DB에 없으면 TMDB에서 데이터 가져와서 DB에 저장
          axios({
            method: 'get',
            url: `${MOVIE_URL}/${this.$route.params.movie_id}`,
            params: {
              api_key: process.env.VUE_APP_TMDB,
              language: 'ko-KR',
            },
          })
          .then((res) => {
            // console.log(res.data)
            this.movie = res.data
          })
          .catch((err) => {
            console.log(err)
          })

          axios({
            method: 'post',
            url: API_URL + '/movies',
            data: {
              title: this.movie['title'],
              overview: this.movie['overview'],
              release_date: this.movie['release_date'],
              tmdb_id: this.movie['id'],
              adult: this.movie['adult'],
              popularity: this.movie['popularity'],
              vote_average: this.movie['vote_average'],
              vote_count: this.movie['vote_count'],
              poster_path: this.movie['poster_path'],
              backdrop_path: this.movie['backdrop_path'],
            }
          })
          .then((response) => {
            console.log(response)
            // this.actionMovies = this.shuffle(response.data)
          })
          .catch((error) => {
            console.log(error)
          })
        }
      })
      .catch((error) => {
        console.log(error)
      })
    },
    getCredits() {
      axios({
        method: 'get',
        url: `${MOVIE_URL}/${this.$route.params.movie_id}/credits`,
        params: {
          api_key: process.env.VUE_APP_TMDB,
          language: 'ko-KR',
        },
      })
        .then((res) => {
          if (res.data.cast.length > 5) {
            this.cast = res.data.cast.slice(0, 5)
          } else {
            this.cast = res.data.cast
          }
          console.log(this.cast)
          this.director = res.data.crew.filter((person) => {
            return person['job'] === 'Director'
          })[0]
          // console.log(res.data.crew.filter((person) => {
          //   return person['job'] === 'Director'
          // })[0]
          // )
          console.log(this.director)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style lang="scss">
.background-img {
  width: 100vw;
  height: 100vh;
  object-fit: cover;
  position: absolute;
  top: 0;
  opacity: 0.4;
  background: #aeaeae;
}

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