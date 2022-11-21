import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import api from "@/api/api"
import router from "@/router"

import { BootstrapVue, IconsPlugin, FormRatingPlugin } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Vuex)
Vue.use(BootstrapVue, IconsPlugin, FormRatingPlugin)

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      // key: 'vuex',              
      // reducer (val) {                                
      //   if(val.authentication.token === null) { // return empty state when user logged out                
      //     return {}
      //   }
      //   return val
      // }
    })
  ],
  state: {
    token: null,
    currUser: null,
    profile: null,

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
    query: '',
    searchResults: '',
    currentMoviePk: null,
    selectedMovies: [],
  },
  getters: {
    isLogin: state => !!state.token,
    shuffledRecommendMovies(state) {
      const arr = state.recommendMovies
      let m = arr.length;
      while (m) {
        const i = Math.floor(Math.random() * m--);
        [arr[m], arr[i]] = [arr[i], arr[m]];
      }
      return arr
    },
    shuffledNowPlayingMovies(state) {
      const arr = state.nowPlayingMovies
      let m = arr.length;
      while (m) {
        const i = Math.floor(Math.random() * m--);
        [arr[m], arr[i]] = [arr[i], arr[m]];
      }
      return arr
    },
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    REMOVE_TOKEN(state) {
      state.token = null
      state.currUser = null
      localStorage.removeItem('vuex')
    },
    SAVE_USER_DATA(state, userData) {
      state.currUser = userData
    },

    SAVE_RECOMMEND: (state, payload) => state.recommendMovies = payload,
    SAVE_NOW_PLAYING: (state, payload) => state.nowPlayingMovies = payload,
    SAVE_ACTION: (state, payload) => state.actionMovies = payload,
    SAVE_ROMANCE: (state, payload) => state.romanceMovies = payload,
    SET_SEARCH_RESULTS: (state, payload) => state.searchResults = payload,
  },
  actions: {
    //////////////// accounts ////////////////
    signUp(context, userData) {
      const formData = new FormData()
      formData.append('username', userData.userId)
      formData.append('nickname', userData.nickname)
      formData.append('password1', userData.password1)
      formData.append('password2', userData.password2)
      formData.append('profile_image', userData.profile_image)

      axios({
        method: 'post',
        url: api.accounts.signup(),
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data',
        }
      })
        .then((res) => {
          const token = res.data.key
          context.commit('SAVE_TOKEN', token) // token
          context.dispatch('getCurrUser', token)
          router.push({ name: 'MainView' })
        })
        .catch((err) => {
          console.log(err)
          alert(err.message)
        })
    },
    logIn(context, userData) {
      axios({
        method: 'post',
        url: api.accounts.login(),
        data: {
          username: userData.userId,
          password: userData.password,
        }
      })
        .then((res) => {
          const token = res.data.key
          context.commit('SAVE_TOKEN', token) // token
          // 로그인되면 유저 정보 가지러가기
          context.dispatch('getCurrUser', token)
          // 이전 페이지로는 어케가징 ?
          router.push({ name: 'MainView' })
        })
        .catch((err) => {
          console.log(err)
          alert('아이디 혹은 비밀번호가 일치하지 않아요!')
        })
    },
    logOut(context, userData) {
      axios({
        method: 'post',
        url: api.accounts.logout(),
        data: userData,
      })
        .then(() => {
          context.commit('REMOVE_TOKEN')
          // alert('로그아웃 완료')
          router.push({ name: 'MainView' })
        })
        .catch((err) => {
          console.log(err)
          // alert(err.message)
        })
    },
    getCurrUser(context, token) {
      console.log('유저정보 가져올게')
      if (context.getters.isLogin) {
        axios({
          method: 'get',
          url: api.accounts.currUserData(),
          headers: {
            Authorization: `Token ${ token }`
          }
        })
          .then((res) => {
            console.log(res.data)
            context.commit('SAVE_USER_DATA', res.data)
          })
          .catch((err) => {
            console.log(err)
            alert(err.message)
            context.commit('REMOVE_TOKEN')
            router.push({ name: 'LogInView' })
          })
      }
    },

    //////////////// movies ////////////////
    fetchRecommendMovies(context) {
      // 로그인 했다면 맞춤 추천, 안했다면 TMDB 추천
      if (this.state.token) {
        axios({
          method: 'get',
          url: api.movies.recommendMovies(),
        })
          .then((res) => {
            // console.log(res)
            context.commit('SAVE_RECOMMEND', res)
          })
          .catch((error) => {
            console.log(error)
          })
      } else {
        const MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'
        axios({
          method: 'get',
          // url: api.movies.recommendMovies(),
          url: MOVIE_URL,
          params: {
            api_key : process.env.VUE_APP_TMDB,
            language: 'ko-KR',
          }
        })
          .then((res) => {
            // console.log(res)
            // context.commit('SAVE_RECOMMEND', res)
  
            // console.log(res.data.results)
            context.commit('SAVE_RECOMMEND', res.data.results)
          })
          .catch((error) => {
            console.log(error)
          })
      }
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
          let res = response.data.results
          // console.log(res)
          context.commit('SAVE_NOW_PLAYING', res)
          // console.log(context.state.nowPlayingMovies)
          for (const movie of res) {
            // DB에 있다면 DB 정보 가져오기
            const API_URL = 'http://127.0.0.1:8000'
            axios.get(API_URL + `/movies/${movie.id}/`)
            .then(() => {
              // console.log(res.data)
              // this.movie = res.data
            })
            .catch((error) => {
              console.log('DB에 없어')
              console.log(error)

              // DB에 없으면 TMDB에서 가져온 데이터를 DB에 저장
              console.log('저장하러간다')
              axios({
                method: 'post',
                url: API_URL + '/movies/',
                headers: {
                  Authorization: `Token ${this.token}`
                },
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
                  console.log('저장완료', response)
                })
                .catch((error) => {
                  console.log('아직 post 없음', error)
                })
            })
        }
      })
        .catch((error) => {
          console.log(error)
        })
    },
    fetchActionMovies(context) {
      axios({
        mehod: 'get',
        url: api.movies.actionMovies()
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
        url: api.movies.romanceMovies()
      })
        .then((response) => {
          // console.log(response.data)
          context.commit('SAVE_ROMANCE', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    showSearchPage(context, query) {  
      axios.get(`https://api.themoviedb.org/3/search/movie?api_key=${process.env.VUE_APP_TMDB}&language=ko&query=` + query + '&include_adult=false')
        .then((res) => {
          context.commit('SET_SEARCH_RESULTS', res.data.results)
          router.push({name: 'MovieSearchView', params: { query: query }})
        })
        .catch((err) => {
          console.log(err)
          console.log('서치에러')
        })
    }
  },
})
