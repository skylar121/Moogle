<template>
    <main >
      <div class="container">
        <div v-if="profileReviews && profileReviews?.length > 0" class="gallery">
          <ProfileReviewItem v-for="review in profileReviews" :key="review.id" :review="review" @click="goToDetail"  />
        </div>
        <div v-else class="gallery w-100">
          <!-- <div class="loader d-block"></div> -->
          <div>아직 남긴 리뷰가 없어요!</div>
        </div>
      </div>
    </main>
</template>

<script>
import { mapState } from 'vuex'
import ProfileReviewItem from '@/components/profile/ProfileReviewItem'

export default {
  name: 'ProfileReviewList',
  components: {
    ProfileReviewItem,
  },
  props: {
    profileReviews: Array,
  },
  computed: {
    ...mapState([
      'userLikes',
    ]),
  },
  methods: {
    goToDetail(id) {
      // console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: id }})
    },
  },
}
</script>

<style>
#v-pills-tabcontent {
  width: 100%;
}

</style>