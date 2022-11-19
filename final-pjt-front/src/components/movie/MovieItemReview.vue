<template>
  <div class="container mb-3 p-4">
    <div v-if="!isLogin">
      <form @submit.prevent="createReview" class="position-relative">
        <div class="star-box d-flex align-items-center ms-2 mb-3">
          <b-form-rating
            id="rating-lg-no-border rating-inline"
            @change="onRate()"
            v-model="movieRating"
            :value="movieRating"
            icon-half="star-half"
            variant="danger"
            no-border inline show-value 
            precision="1"
            class="star text-light"
            size="lg"
            color="#ff8800"
          ></b-form-rating>
        </div>
        <div class="mb-3 review-input">
          <label for="review" class="form-label">나의 한줄평</label>
          <input type="text" id="review">
        </div>
        <div class="mb-5 form-check review-check">
          <input type="checkbox" class="form-check-input" id="private">
          <label class="form-check-label me-2" for="private">비공개</label>
          <span id="emailHelp" class="form-text">나만 볼 수 있어요.</span>
        </div>
        <button type="submit" class="btn btn-primary position-absolute review-submit-btn"><i class="fa-solid fa-pen-to-square"></i></button>
      </form>
    </div>

    <div v-else class="my-3">
      <button type="button" class="btn btn-outline-primary">
        <router-link :to="{ name: 'LogInView' }" class="">
        별점 & 리뷰를 남기려면 로그인하러 가기 🐱
        </router-link>
      </button>
    </div>

  </div>
</template>

<script>
import { mapState } from 'vuex'
import { BFormRating } from 'bootstrap-vue'
export default {
  name: 'MovieItemReview',
  components: {
    BFormRating
  },
  data() {
    return {
      movieId: this.$route.params.movie_id,
      movieRating: 0,
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    onRate() {

    },
    getReview() {

    },
    createReview() {

    },
  },
  computed: {
    ...mapState([
      'userNickname',
      'isLogin',
    ]),
    // shuffleRecommendMovies() {
    //   return this.shuffle(this.recommendMovies)
    // },
  },

}
</script>

<style>
.review-input input {
  color: white;
  width: 100%;
  border-bottom: 1px solid #BF93FF;
  outline: none;
  margin-bottom: 1.2em;
}

.review-check input {
  border: 1px solid white;
}

.review-submit-btn {
  position: absolute;
  bottom: -1.5em;
  right: 0;
}



</style>