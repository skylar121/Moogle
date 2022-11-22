const LOCAL = 'http://127.0.0.1:8000/'

const ACCOUNTS = 'accounts/'
const CUSTOM = 'account/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => LOCAL + ACCOUNTS + 'login/',
    logout: () => LOCAL + ACCOUNTS + 'logout/',
    signup: () => LOCAL + ACCOUNTS + 'signup/',
    // 유저 정보 가져오기
    // currUserData: username => LOCAL + ACCOUNTS + 'userinfo/' + username,
    currUserName: () => LOCAL + ACCOUNTS + 'user/',
    currUserInfo: (username) => LOCAL + ACCOUNTS + 'userinfo/' + username,
    // 기본 유저 정보
    profile: username => LOCAL + ACCOUNTS + username + '/',
    // 팔로우, 언팔로우
    follow: username => LOCAL + CUSTOM + username + 'follow/',
    // follow: id => LOCAL + ACCOUNTS + id + '/',
    // 팔로우 초기값
    follower: username => LOCAL + ACCOUNTS + 'follower' + username + '/',
    following: username => LOCAL + ACCOUNTS + 'following' + username + '/',
  },
  movies: {
    recommendMovies: () => LOCAL + MOVIES + 'recommend/',
    nowPlayingMovies: () => LOCAL + MOVIES + 'goto_main/',
    actionMovies: () => LOCAL + MOVIES + 'action10/',
    romanceMovies: () => LOCAL + MOVIES + 'romance10/',
    createReview: movieId => LOCAL + MOVIES + movieId + '/review_list_create/',
    updateDeleteReview: reviewId => LOCAL + MOVIES + 'review/' + reviewId + '/',
    // 영화 리뷰 좋아요
    toggleReviewLike: reviewId => LOCAL + MOVIES + reviewId + '/like_toggle/',
    // 영화 리뷰 좋아요 초기값
    getReviewCount: reviewId => LOCAL + MOVIES + reviewId + '/like_count/',
    // 유저가 쓴 리뷰 및 프로필에 보여줄 정보
    getUserProfile: username => LOCAL + MOVIES + 'profile/' + username + '/',
  },
}