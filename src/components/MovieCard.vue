<template>
  <div class="div" @mouseenter="showModal" @mouseleave="isHovered=false">
    <img 
      :src="'https://image.tmdb.org/t/p/original'+movie.poster_path" class="card-img-top" 
      alt=""
      >
    <div class="">
      <h5 class="">{{ movie.title }}</h5>
      <!-- <p class="">
        {{movie.overview.substr(0, 100)}}...
      </p> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  data() {
    return {
      videoUrl: null,
      isHovered: false,
    }
  },
  methods: {
    showModal() {
      this.videoUrl = `https://www.youtube.com/results?search_query=${this.movie.title} 공식 예고편`
      this.isHovered = true
      this.$emit('show-modal', this.isHovered, this.videoUrl)
      // console.log('MovieCard에서 감지')
    },
  },
}
</script>

<style>
.div {
  width: 300px;
}

img {
	width: 100%;
	pointer-events: none;
	z-index: 999;
	cursor: pointer;
}
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 999;
  width: 80vw;
  height: 80vh;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
}
</style>