import api from "@/api/api"
import router from "@/router"
import axios from "axios"

export default {
  state: {
    token: null,
    currUser: null,
    profile: null,
  },
  getters: {
    isLogin: state => !!state.token,
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
    },
    REMOVE_TOKEN(state) {
      state.token = null
      localStorage.removeItem("vuex")
    },
    SAVE_USER_DATA(state, userData) {
      state.currUser = userData
    }
  },
  actions: {
    signUp(context, userData) {
      axios({
        method: 'post',
        url: api.accounts.signup(),
        data: userData,
      })
        .then((res) => {
          const token = res.data.key
          context.commit('SAVE_TOKEN', token) // token
          context.dispatch('getCurrUser', token)
          router.push({ name: 'MainView' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logIn(context, userData) {
      axios({
        method: 'post',
        url: api.accounts.login(),
        data: {
          id: userData.id,
          password: userData.password,
        }
      })
        .then((res) => {
          const token = res.data.key
          context.commit('SAVE_TOKEN', token) // token
          context.dispatch('getCurrUser', token)
          // 이전 페이지로 router.push ?
          // router.push({ name: 'MainView' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logOut(context) {
      context.commit('REMOVE_TOKEN')
    },
    getCurrUser(context, token) {
      if (context.getters.isLogin) {
        axios({
          method: 'get',
          // 유저정보 가져오는 url 상의 필요
          url: api.accounts.currUserData(),
          headers: {
            "X-AUTH-TOKEN": token
          }
        })
          .then((res) => {
            context.commit('SAVE_USER_DATA', res)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    }
  },
}