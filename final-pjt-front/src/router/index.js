import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: MovieView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
