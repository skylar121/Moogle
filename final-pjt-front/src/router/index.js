import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '@/views/movie/MainView'
import SignUpView from '@/views/accounts/SignUpView'
import LogInView from '@/views/accounts/LogInView'
import ProfileView from '@/views/accounts/ProfileView'
import DetailView from '@/views/movie/DetailView'
import ReviewDetailView from '@/views/movie/ReviewDetailView'
import MovieSearchView from '@/views/movie/MovieSearchView'
import NotFoundView from '@/views/NotFoundView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainView',
    component: MainView
  },
  {
    path: '/movie/:movie_id',
    name: 'DetailView',
    component: DetailView
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
  {
    path: '/profile/:username',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/review/:review_id',
    name: 'ReviewDetailView',
    component: ReviewDetailView
  },
  {
    path: '/search/:query',
    name: 'MovieSearchView',
    component: MovieSearchView
  },
  {
    path: '/404',
    name: 'NotFound',
    component: NotFoundView
  },
  {
    path: '*',
    redirect: '/404',
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach((to, from, next) => {
//   const isLogIn = this.$store.getters.isLogin

//   // 로그인이 필요한 페이지
//   // const authPages = ['hello', 'home', 'about']
//   const allowAllPages = ['login']
//   // 앞으로 방문할 페이지가 인증을 필요로 하는 사이트인지 검사
//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allowAllPages.includes(to.name)

//   if (isAuthRequired && !isLogIn) {
//     console.log('Login으로 이동!')
//     next({ name: 'login'})
//   } else {
//     console.log('to로 이동!')
//     next()
//   }
// })

export default router
