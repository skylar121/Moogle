<template>
    <main >
      <div class="container">
        <div v-if="userReviews && userReviews?.length > 0" class="gallery">
          <ProfileReviewItem v-for="review in userReviews" :key="review.id" :review="review" @click="goToDetail"  />
        </div>
        <div v-else class="gallery w-100">
          <div class="loader d-block"></div>
          <div>아직 남긴 리뷰가 없어요! 첫번째 리뷰를 남기러 갈까요?</div>
        </div>
      </div>
    </main>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ProfileReviewItem from '@/components/profile/ProfileReviewItem'

export default {
  name: 'ProfileReviewList',
  components: {
    ProfileReviewItem,
  },
  computed: {
    ...mapState([
      'userReviews',  // 로그인 유저 (리뷰 정보)
      'userLikes',  // 로그인 유저 (리뷰 정보)
    ]),
  },
  methods: {
    ...mapActions([
      'getUserReviews',
      'getUserLikes',
    ]),
    goToDetail(id) {
      // console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: id }})
    },
  },
  created() {
    this.getUserLikes()
    this.getUserReviews()
  }
}
</script>

<style>
#v-pills-tabcontent {
  width: 100%;
}

</style>