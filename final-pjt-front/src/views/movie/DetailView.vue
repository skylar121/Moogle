<template>
  <div v-if="movie">
    <picture><img class="background-img" :src="movie.backdrop_path ? 'https://image.tmdb.org/t/p/original' + movie.backdrop_path : 'https://image.tmdb.org/t/p/original' + movie.poster_path"></picture>
    <div class="container-lg mt-3">
      <div class="card mb-3">
        <!-- 영화 디테일 + 리뷰 작성 + 추천 -->
        <div class="row g-0">
          <!-- 왼쪽 포스터 영역 -->
          <div class="col-md-4">
            <img :src="movie.poster_path ? 'https://image.tmdb.org/t/p/original' + movie.poster_path : 'https://image.tmdb.org/t/p/original' + movie.backdrop_path" class="img-fluid rounded-start  w-100" alt="">
            <MovieCreateReview :movie="movie" :userReview="userReview" :propStar="userReview ? userReview[0]?.rank : 0" :propContent="userReview ? userReview[0]?.content : null" @fetchAllReviews="fetchAllReviews" />
          </div>
          <!-- 오른쪽 영역 -->
          <div class="col-md-8">
            <div class="card-body p-4">
              <MovieDetail :movie="movie" :cast="cast" :director="director" />
              <MovieSimilar />
            </div>
          </div>
        </div>
        <!-- 영화 리뷰 목록 -->
        <MovieReviewList :reviews="reviews" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '@/api/api'
import axios from 'axios'
import MovieCreateReview from '@/components/movie/MovieCreateReview'
import MovieDetail from '@/components/movie/MovieDetail'
import MovieSimilar from '@/components/movie/MovieSimilar'
import MovieReviewList from '@/components/movie/MovieReviewList'

const MOVIE_URL = 'https://api.themoviedb.org/3/movie'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    MovieDetail,
    MovieSimilar,
    MovieReviewList,
    MovieCreateReview,
  },
  data() {
    return {
      movie: null,
      cast: null,
      director: null,
      userReview: null,
      totalComments: null,
      reviews: null,
    }
  },
  computed: {
    ...mapState([
      'token',
      'currUser',
    ]),
  },
  created() {
    this.getMovieDetail()
    this.getCredits()
    this.fetchAllReviews()
  },
  methods: {
    getMovieDetail() {
      axios.get(API_URL + `/movies/${this.$route.params.movie_id}/`)
      .then((res) => {
        // DB에 있다면 DB 정보 가져오기
        // console.log(res.data)
        this.movie = res.data
      })
      .catch((error) => {
        // console.log('DB에 없어')
        console.log(error)

        // DB에 없으면 TMDB에서 데이터 가져와서 DB에 저장
        if (!this.movie) {
          // console.log('TMDB에서 가져올거야')
          axios({
            method: 'get',
            url: `${MOVIE_URL}/${this.$route.params.movie_id}`,
            params: {
              api_key: process.env.VUE_APP_TMDB,
              language: 'ko-KR',
            },
          })
          .then((res) => {
            this.movie = res.data
            // console.log(this.movie)

            axios({
              method: 'post',
              url: API_URL + '/movies/',
              data: {
                title: this.movie['title'],
                overview: this.movie['overview'],
                release_date: this.movie['release_date'],
                id: this.movie['id'],
                adult: this.movie['adult'],
                popularity: this.movie['popularity'],
                vote_average: this.movie['vote_average'],
                vote_count: this.movie['vote_count'],
                poster_path: this.movie['poster_path'],
                backdrop_path: this.movie['backdrop_path'],
              }
            })
              .then((response) => {
                // console.log(this.movie)
                console.log(response)
              })
              .catch((error) => {
                console.log('아직 post 없음', error)
              })
          })
          .catch((err) => {
            console.log(err)
          })
        }
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
          this.director = res.data.crew.filter((person) => {
            return person['job'] === 'Director'
          })[0]
          // console.log(res.data.crew.filter((person) => {
          //   return person['job'] === 'Director'
          // })[0]
          // )
          // console.log(this.director)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 유저 리뷰 가져오기
    fetchAllReviews() {
      if (this.token) {
        console.log('1')
        axios({
        method: 'get',
        url: api.movies.createReview(this.$route.params.movie_id),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((response)=>{
          console.log(response.data)
          this.reviews = response.data.reverse()
          this.userReview = response.data.filter(review => this.currUser.pk === review.user)
          console.log(this.userReview)
        })
        .catch((error)=>{
          console.log(error);
        })
      }
    },
  },
}
</script>

<style lang="scss">
#app > nav > div:nth-child(3) > a {
  color: $primary;
}

.background-img {
  width: 100%;
  height: 160%;
  object-fit: cover;
  position: absolute;
  top: 0;
  opacity: 0.4;
  background: #575757;
  /* background-image: linear-gradient(rgba(0,0,0,.85) 15%,rgba(0,0,0,.2) 40%,#000 90%); */
}

/* background-image로 구현시
  background-image: linear-gradient(rgba(0,0,0,.85) 15%,rgba(0,0,0,.2) 40%,#000 90%);
  background-attachment: fixed;
  margin: 0;
  height: 100vh; */

.card {
  background: $body-bg;
  border: none;
  .card-title {
    font-size: 2.7rem;
    font-weight: 800;
  }
  & a {
    color: white;
  }
  h6 {
    color: $primary;
  }
}
</style>