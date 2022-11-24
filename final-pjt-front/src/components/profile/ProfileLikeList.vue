<template>
    <main>
      <div class="container">
        <div  v-if="userLikes && userLikes?.length > 0"  class="gallery">
          <ProfileLikeItem v-for="likedMovie in userLikes" :key="likedMovie.id" :likedMovie="likedMovie" @click="goToDetail"  />
        </div>
        <div v-else class="gallery w-100">
          <div class="loader d-block"></div>
          <div>아직 좋아요 한 영화가 없어요! 추천 영화는 어떤가요?</div>
        </div>
      </div>
      <hr>
    </main>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import ProfileLikeItem from '@/components/profile/ProfileLikeItem'

export default {
  name: 'ProfileLikeList',
  components: {
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
#v-pills-tabcontent {
  width: 100%;
}
</style>