import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

import { BootstrapVue, IconsPlugin, FormRatingPlugin } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Vuex)
Vue.use(BootstrapVue, IconsPlugin, FormRatingPlugin)

import accounts from './modules/accounts'
import movies from './modules/movies'

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  modules: {
    accounts,
    movies,
  },
  state: {
    recommendMovies: null,
  },
  mutations: {
    SAVE_MOVIE_DATA(state, payload) {
      state.recommendMovies = payload
    },
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
  },
})
