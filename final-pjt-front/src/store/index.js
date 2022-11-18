import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    isLogin: false,
    userNickname: null,
    recommendMovies: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    SAVE_MOVIE_DATA(state, payload) {
      state.recommendMovies = payload
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      // 메인 페이지로 보내기
      state.isLogin = true
      state.username = 
      router.push({ name: 'MainView' })
    },
    logout(state) {
      state.isLogin = false
      state.token = null
      localStorage.removeItem("vuex")
    }
  },
  actions: {
    fetchMovie(context) {
      // const MOVIE_URL = 'https://api.themoviedb.org/3/movie/top_rated'
      axios({
        method: 'get',
        url: `${API_URL}/movies`,
        // params: {
        //   api_key : process.env.VUE_APP_TMDB,
        //   language: 'ko-KR',
        // }
      })
        .then((response) => {
          console.log(response.data)
          context.commit('SAVE_MOVIE_DATA', response.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          // key 이름과 값 이름이 같으면 생략해도 됨 (js 문법)
          // username,
          // password1,
          // password2,
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key) // token
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key) // token
        })
    },
  },
  modules: {
  }
})
