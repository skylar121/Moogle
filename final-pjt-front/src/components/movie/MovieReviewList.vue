<template>
  <div class="row g-0 p-4 text-center text-primary">
    <h3 class="fw-bold fs-2">All Reviews</h3>
    <div v-if="isLogin && reviews && reviews?.length > 0" class="col">
      <MovieReviewItem v-for="review in reviews" :review="review" :key="review.id" @fetchAllReviews="fetchAllReviews" />
      <!-- <div class="d-flex">
        <nav aria-label="Page navigation example">
          <ul class="pagination justify-content-center" >
            <li class="page-item disabled" style="background-color: #191817">
              <a class="page-link">Previous</a>
            </li>
            <li class="page-item"><a class="page-link" href="">1</a></li>
            <li class="page-item"><a class="page-link" href="">2</a></li>
            <li class="page-item"><a class="page-link" href="">3</a></li>
            <li class="page-item">
              <a class="page-link" href="">Next</a>
            </li>
          </ul>
        </nav>
      </div> -->
    </div>
    <div v-else>
      <p class="text-muted fs-5">아직 리뷰가 없어요 😿 첫번째 리뷰를 남겨주세요!</p>
    </div>
    <div v-if="!isLogin">
      <p>유저들의 리뷰를 보려면 로그인 하세요 😸</p>
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
  methods: {
    fetchAllReviews () {
      this.$emit('fetchAllReviews')
    }
  },
  computed: {
    ...mapGetters([
      'isLogin'
    ]),
  },
  created() {
    this.$emit('fetchAllReviews')
  }
}
</script>

<style lang="scss">

</style>