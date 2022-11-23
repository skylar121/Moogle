<template>
  <div v-if="movie">
    <picture><img class="background-img" :src="movie.backdrop_path ? 'https://image.tmdb.org/t/p/original' + movie.backdrop_path : 'https://image.tmdb.org/t/p/original' + movie.poster_path"></picture>
    <div class="container-lg mt-3">
      <div class="card mb-3">
        <!-- 영화 디테일 + 리뷰 작성 + 추천 -->
        <div class="row g-0">
          <!-- 왼쪽 포스터 영역 -->
          <div class="col-md-4">
            <div id="movie-detail-poster">
                <button v-if="!isLiked" @click="toggleMovieLike"><span span id="movie-detail-like" style="color: #e64949;"><i class="fa-regular fa-heart me-2 fs-1"></i></span></button>
                <button v-else @click="toggleMovieLike"><span span id="movie-detail-like" style="color: #e64949;"><i class="fa-solid fa-heart me-2 fs-1"></i></span></button>
              <img
                :src="movie.poster_path ? 'https://image.tmdb.org/t/p/original' + movie.poster_path : 'https://image.tmdb.org/t/p/original' + movie.backdrop_path" class="img-fluid rounded-start w-100" alt="">
                <MovieCreateReview :movie="movie" :userReview="userReview" @fetchAllReviews="fetchAllReviews"
              />
            </div>
            <!-- <div v-if="userReview">
              <MovieCreateReview :movie="movie" :userReview="userReview" @fetchAllReviews="fetchAllReviews" />
            </div>
            <div v-else>
              <MovieCreateReview :movie="movie" @fetchAllReviews="fetchAllReviews" />
            </div> -->
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
      isLiked: null,
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
    this.getInitialMovieLike()
  },
  methods: {
    toggleMovieLike() {
      axios({
        method: 'get',
        url: api.movies.toggleMovieLike(this.currUser.id, this.$route.params.movie_id),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          this.isLiked = res.data
          console.log(this.isLiked)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getInitialMovieLike() {
      console.log(this.$route.params.movie_id)
      axios({
        method: 'get',
        url: api.movies.getMovieLikedUsers(this.$route.params.movie_id),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.isLiked = Boolean(res.data.filter(follower => follower.username === this.currUser.username).length)
          console.log(this.isLiked)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMovieDetail() {
        axios({
          method: 'get',
          url: API_URL + `/movies/${this.$route.params.movie_id}/`,
        })
        .then((res) => {
          console.log(this.$route.params.movie_id)
          this.movie = res.data
          console.log(res.data)
        })
        .catch((error) => {
          console.log('DB에 없어')
          console.log(error)

          // DB에 없으면 TMDB에서 가져온 데이터를 DB에 저장
          console.log('저장하러간다')
          axios({
            method: 'get',
            url: API_URL + `/movies/${this.$route.params.movie_id}/`,
            data: {
              id: this.$route.params.movie_id,
            }
          })
            .then((response) => {
              // console.log(this.movie)
              console.log('저장완료', response)
            })
            .catch((error) => {
              console.log('저장안돼 ㅠㅠ', error)
            })
        })
      console.log('DB에서 무비디테일가져오기 완료')
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
        axios({
        method: 'get',
        url: api.movies.createReview(this.$route.params.movie_id),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((response)=>{
          // console.log('찐데이터')
          this.reviews = response.data.reverse()
          // console.log(this.reviews)
          this.userReview = response.data.filter(review => this.currUser.username === review.username)
          // console.log(this.userReview)
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

#movie-detail-poster {
  position: relative;
}
#movie-detail-like {
  position: absolute;
  top: 1em;
  left: 1em;
  ::after {
    content: '보고싶어요';
    display: block;
    font-weight: 500;
    margin-top: .3em;
    font-size: .8rem;
    color: #e64949;
    inset: 0;
  }
}

.background-img {
  width: 100%;
  height: 160%;
  object-fit: cover;
  position: absolute;
  top: 0;
  opacity: 0.4;
  background: #575757;
  z-index: -1;
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