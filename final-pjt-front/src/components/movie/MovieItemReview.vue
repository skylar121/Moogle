<template>
  <div>
    <div class="d-flex align-items-center mt-3">
      <span class="text-small">
        내 평점&nbsp;
      </span>
      <div class="star-box">
        <!-- <b-form-rating
          id="rating-lg-no-border rating-inline"
          v-if="isLoggedIn"
          @change="onRate()"
          v-model="value.rate"
          :value="value.rate"
          variant="danger"
          no-border inline show-value show-clear
          class="star"
          size="lg"
        ></b-form-rating> -->
      </div>
    </div>
  </div>
</template>

<script>
// import { BFormRating } from 'bootstrap-vue'
export default {
  name: 'MovieItemReview',
  components: {
    // BFormRating
  },
}
</script>

<style>

</style>