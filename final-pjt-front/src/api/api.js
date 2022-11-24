const LOCAL = 'http://127.0.0.1:8000/'

const ACCOUNTS = 'accounts/'
// const CUSTOM = 'account/'
const MOVIES = 'movies/'

export default {
  accounts: {
    login: () => LOCAL + ACCOUNTS + 'login/',
    logout: () => LOCAL + ACCOUNTS + 'logout/',
    signup: () => LOCAL + ACCOUNTS + 'signup/',
    currUserName: () => LOCAL + ACCOUNTS + 'user/',
    currUserInfo: (username) => LOCAL + ACCOUNTS + 'userinfo/' + username,
    // // 기본 유저 정보
    // profile: username => LOCAL + ACCOUNTS + username + '/',
    // 팔로우, 언팔로우 (팔로우하고자 하는 유저네임)
    follow: username => LOCAL + ACCOUNTS + 'follow/' + username + '/',
    // 팔로워 값
    followers: username => LOCAL + ACCOUNTS + 'followers/' + username +  '/',
    // 팔로잉 값
    followings: username => LOCAL + ACCOUNTS + 'followings/' + username + '/',
  },
  movies: {
    recommendMovies: userId => LOCAL + MOVIES + userId + '/recommend/',
    nowPlayingMovies: () => LOCAL + MOVIES + 'goto_main/',
    actionMovies: () => LOCAL + MOVIES + 'action10/',
    romanceMovies: () => LOCAL + MOVIES + 'romance10/',
    // 영화 좋아요
    toggleMovieLike: (userId, movieId) => LOCAL + MOVIES + userId + '/' + movieId + '/like/',
    // 유저가 좋아한 영화
    getUserLikedMovie: userId => LOCAL + MOVIES + userId + '/like/',
    // 영화에 좋아요 한 유저들
    getMovieLikedUsers: movieId => LOCAL + MOVIES + movieId + '/like/' + 'users/',

    // 리뷰
    createReview: movieId => LOCAL + MOVIES + movieId + '/review_list_create/',
    updateDeleteReview: reviewId => LOCAL + MOVIES + 'review/' + reviewId + '/',
    // 리뷰 댓글
    getReviewComments: reviewId => LOCAL + MOVIES + 'review_comments/' + reviewId + '/',
    createReviewComment: reviewId => LOCAL + MOVIES + reviewId + '/review_comment/',
    deleteReviewComment: (reviewId, commentId) => LOCAL + MOVIES + 'review_comment/' + reviewId + '/' + commentId + '/',

    // 리뷰 좋아요
    toggleReviewLike: reviewId => LOCAL + MOVIES + reviewId + '/like_toggle/',
    // 리뷰 좋아요 개수
    getReviewCount: reviewId => LOCAL + MOVIES + reviewId + '/like_count/',
    // 유저가 쓴 리뷰들
    getUserReviews: username => LOCAL + MOVIES + 'profile/' + username + '/',
  },
}