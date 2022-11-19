const LOCAL = 'http://127.0.0.1:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => LOCAL + ACCOUNTS + 'login/',
    logout: () => LOCAL + ACCOUNTS + 'logout/',
    signup: () => LOCAL + ACCOUNTS + 'signup/',
    currUserData: () => LOCAL + ACCOUNTS + 'user/',
    profile: id => LOCAL + ACCOUNTS + id + '/',
    follow: id => LOCAL + ACCOUNTS + id + '/',
    userMovieData: id => LOCAL + ACCOUNTS + id + '/movies/',
  },
  movies: {
    recommendMovies: () => LOCAL + MOVIES + 'recommend/',
    nowPlayingMovies: () => LOCAL + MOVIES + 'goto_main/',
    actionMovies: () => LOCAL + MOVIES + 'action10/',
    romanceMovies: () => LOCAL + MOVIES + 'romance10/',
  },
}