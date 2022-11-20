<template>
  <div class="row g-0 p-4">
    <h3 class="fw-bold">Reviews</h3>
    <span>더 많은 게시물을 보려면? Community 가기</span>
    <div class="container overflow-hidden">
      <div v-if="isLogin" class="row col-6 col-md-4 p-3">
        <div v-if="reviews?.length > 0" class="col">
          <div v-for="review in reviews" :key="review.id" class="card review-card ">
            <div class="card-header text-bg-primary">
              {{ review.userName }}
            </div>
            <div class="card-body d-flex flex-column justify-content-center align-items-center">
              <div class="movieVoteAverage">
                <b-form-rating
                  :value="review.rank"
                  readonly
                  show-value
                  precision="1"
                  color="#ffd21e"
                  class="border-0 text-light"
                ></b-form-rating>
                <!-- <p>{{ movie?.vote_average.toFixed(1) > 0.0 ? `⭐${movie?.vote_average.toFixed(1)} / 10` : '아직 별점이 없어요!' }} </p> -->
              </div>
              <p class="card-text">{{ review.content }}</p>
              <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
            </div>
            <div class="card-footer text-muted d-flex justify-content-between">
              <div class="fs-5">
                <i class="fa-regular fa-heart me-2"></i>
                <i class="fa-regular fa-comment me-2"></i>
                <i v-if="currUser.pk === review.user" @click="updateReview" class="fa-solid fa-pencil me-2"></i>
                <i v-if="currUser.pk === review.user" @click="deleteReview" class="fa-solid fa-trash-can"></i>
              </div>
              {{ review.updated_at.slice(0, 10) }}
            </div>
          </div>
        </div>
        <div v-else>
          <p>아직 리뷰가 없어요ㅠㅠ</p>
        </div>
      </div>
      <div v-else>
        <p>유저들의 리뷰를 보려면 로그인 하세요</p>
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapGetters } from 'vuex';
export default {
  name: 'MovieReviewList',
  props: {
    reviews: Array,
  },
  computed: {
    ...mapState([
      'currUser'
    ]),
    ...mapGetters([
      'isLogin'
    ])
  },
  methods: {
    updateReview() {

    },
    deleteReview() {
      axios({
        method: 'delete',
        url: '',
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
      .then(() => {
        
      })
      .catch(() => {
        console.log()
      })
    }
  },
  created() {
    this.$emit('fetchAllReviews')
  }
}
</script>

<style lang="scss">

</style>