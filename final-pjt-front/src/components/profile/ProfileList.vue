<template>
    <main>
      <div>REVIEWS</div>
      <div class="container">
        <div class="gallery">
          <ProfileReviewItem v-for="review in userReviews" :key="review.id" :review="review" @click="goToDetail"  />
        </div>
        <!-- <div class="loader"></div> -->
      </div>
      <hr>
      <div>LIKES</div>
      <div class="container">
        <div class="gallery">
          <ProfileLikeItem v-for="likedMovie in userLikes" :key="likedMovie.id" :likedMovie="likedMovie" @click="goToDetail"  />
        </div>
        <!-- <div class="loader"></div> -->
      </div>
    </main>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ProfileReviewItem from '@/components/profile/ProfileReviewItem'
import ProfileLikeItem from '@/components/profile/ProfileLikeItem'

export default {
  name: 'ProfileList',
  components: {
    ProfileReviewItem,
    ProfileLikeItem,
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

</style>