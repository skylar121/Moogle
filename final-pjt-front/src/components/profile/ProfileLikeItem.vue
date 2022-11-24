<template>
  <div @click="goToDetail" class="gallery-item" tabindex="0">
    <img :src="likedMovie?.backdrop_path ? 'https://image.tmdb.org/t/p/original' + likedMovie?.backdrop_path : 'https://image.tmdb.org/t/p/original' + likedMovie?.poster_path" class="gallery-image" alt="">
    <div class="gallery-item-info">
      <ul>
        <div class="mx-auto my-0 text-center">
          <li class="gallery-item-likes">{{ likedMovie?.title }}</li>
          <div class="mx-auto my-0 text-center">
            <li class="gallery-item-likes"><i class="fas fa-heart" aria-hidden="true"></i><span class="me-4"> {{ likedMovie?.like_users?.length }}</span></li>
            <!-- <li class="gallery-item-comments"><i class="fas fa-comment" aria-hidden="true"></i> 댓글개수</li> -->
          </div>
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileReviewItem',
  props: {
    likedMovie: Object,
  },
  methods: {
    goToDetail() {
      // console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: this.likedMovie.id }})
    }
  },
}
</script>

<style>

</style>