<template>
    <main>
      <div class="container">
        <div  v-if="profileLikes && profileLikes?.length > 0"  class="gallery">
          <ProfileLikeItem v-for="likedMovie in profileLikes" :key="likedMovie.id" :likedMovie="likedMovie" @click="goToDetail"  />
        </div>
        <div v-else class="gallery w-100">
          <!-- <div class="loader d-block"></div> -->
          <div>아직 좋아요 한 영화가 없어요!</div>
        </div>
      </div>
    </main>
</template>

<script>
import { mapState } from 'vuex'
import ProfileLikeItem from '@/components/profile/ProfileLikeItem'

export default {
  name: 'ProfileLikeList',
  components: {
    ProfileLikeItem,
  },
  props: {
    profileLikes: Array,
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