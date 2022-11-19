import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import api from "@/api/api"

import { BootstrapVue, IconsPlugin, FormRatingPlugin } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Vuex)
Vue.use(BootstrapVue, IconsPlugin, FormRatingPlugin)

import accounts from './modules/accounts'
import movies from './modules/movie'

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
  },
})
