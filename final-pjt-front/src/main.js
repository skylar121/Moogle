import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import gsap from 'gsap'

Vue.config.productionTip = false

// Vue.prototype에 Vue 인스턴스 메서드를 연결
// Vue.prototype.$gsap = gsap;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
