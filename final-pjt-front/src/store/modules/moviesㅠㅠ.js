import api from "@/api/api"
// import router from "@/router"
import axios from "axios"

export default {
  state: {
    recommendMovies: null,
    nowPlayingMovies: null,
    actionMovies: null,
    romanceMovies: null,
    genres_list: [
      {
          "id": 28,
          "name": "액션"
      },
      {
          "id": 12,
          "name": "모험"
      },
      {
          "id": 16,
          "name": "애니메이션"
      },
      {
          "id": 35,
          "name": "코미디"
      },
      {
          "id": 80,
          "name": "범죄"
      },
      {
          "id": 99,
          "name": "다큐멘터리"
      },
      {
          "id": 18,
          "name": "드라마"
      },
      {
          "id": 10751,
          "name": "가족"
      },
      {
          "id": 14,
          "name": "판타지"
      },
      {
          "id": 36,
          "name": "역사"
      },
      {
          "id": 27,
          "name": "공포"
      },
      {
          "id": 10402,
          "name": "음악"
      },
      {
          "id": 9648,
          "name": "미스터리"
      },
      {
          "id": 10749,
          "name": "로맨스"
      },
      {
          "id": 878,
          "name": "SF"
      },
      {
          "id": 10770,
          "name": "TV 영화"
      },
      {
          "id": 53,
          "name": "스릴러"
      },
      {
          "id": 10752,
          "name": "전쟁"
      },
      {
          "id": 37,
          "name": "서부"
      }
    ],
  },
  mutations: {
    SAVE_RECOMMEND: (state, payload) => state.recommendMovies = payload,
    SAVE_NOW_PLAYING: (state, payload) => state.nowPlayingMovies = payload,
    SAVE_ACTION: (state, payload) => state.actionMovies = payload,
    SAVE_ROMANCE: (state, payload) => state.romanceMovies = payload,
  },
  actions: {
    fetchRecommendMovies(context) {
      axios({
        method: 'get',
        url: api.movies.recommendMovies(),
      })
        .then((response) => {
          console.log(response)
          context.commit('SAVE_RECOMMEND', response)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    fetchNowPlayingMovies(context) {
      const MOVIE_URL = 'https://api.themoviedb.org/3/movie/now_playing'
      axios({
        method: 'get',
        // url: api.movies.nowPlayingMovies(),
        url: MOVIE_URL,
        params: {
          api_key : process.env.VUE_APP_TMDB,
          language: 'ko-KR',
        }
      })
        .then((response) => {
          console.log(response.data.results)
          context.commit('SAVE_NOW_PLAYING', response.data.results)
          console.log(context.state.nowPlayingMovies)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    fetchActionMovies(context) {
      axios({
        mehod: 'get',
        url: api.movies.nowPlayingMovies()
      })
        .then((response) => {
          console.log(response.data)
          context.commit('SAVE_ACTION', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    fetchRomanceMovies(context) {
      axios({
        mehod: 'get',
        url: api.movies.nowPlayingMovies()
      })
        .then((response) => {
          console.log(response.data)
          context.commit('SAVE_ROMANCE', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}