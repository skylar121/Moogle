<template>
  <div class="row g-0 p-4">
    <h3 class="fw-bold">Reviews</h3>
    <div class="container overflow-hidden">
      <div v-if="isLogin" class="row col-6 col-md-4 p-3">
        <div v-if="reviews && reviews.length > 0" class="col">
          <MovieReviewItem v-for="review in reviews" :review="review" :key="review.id" />
        </div>
        <div v-else>
          <p>아직 리뷰가 없어요ㅠㅠ</p>
        </div>
      </div>
      <div v-else>
        <p>유저들의 리뷰를 보려면 로그인 하세요~!</p>
      </div>
    </div>
    
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import MovieReviewItem from '@/components/movie/MovieReviewItem'

export default {
  name: 'MovieReviewList',
  components: {
    MovieReviewItem,
  },
  props: {
    reviews: Array,
  },
  computed: {
    ...mapGetters([
      'isLogin'
    ]),
  },
  methods: {
    // likeReview() {
    //   axios({
    //     method: 'get',
    //     url: api.movies.likeReview()
    //   })
    // },
    // deleteReview() {
    //   if (confirm('진짜 삭제할까요?') === true) {
    //     axios({
    //       method: 'delete',
    //       url: api.movies.updateDeleteReview(this.userReview[0].id),
    //       headers: {
    //         Authorization: `Token ${this.token}`
    //       }
    //     })
    //       .then(() => {
    //         // console.log(res)
    //         alert('정상적으로 삭제되었어요.')
    //         this.isEditing = false
    //         this.$emit('fetchAllReviews')
    //       })
    //       .catch((err) => {
    //         console.log(err)
    //       })
    //     }
    // },
  },
  created() {
    this.$emit('fetchAllReviews')
  }
}
</script>

<style lang="scss">

</style>