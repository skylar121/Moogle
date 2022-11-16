import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieData: null,
  },
  getters: {
  },
  mutations: {
    SAVE_MOVIE_DATA(state, payload) {
      state.movieData = payload
    }
  },
  actions: {
    fetchMovie(context) {
      const MOVIE_URL = 'https://api.themoviedb.org/3/movie/top_rated'
      axios.get(MOVIE_URL, {
        params: {
        api_key : process.env.VUE_APP_TMDB,
        language: 'ko-KR',
        }
      })
        .then((response) => {
          console.log(response.data.results)
          context.commit('SAVE_MOVIE_DATA', response.data.results)
          
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  modules: {
  }
})
