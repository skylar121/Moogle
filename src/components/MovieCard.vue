<template>
  <div>
    <div class="card" 
      style="width: 18rem;"
      @mouseenter="showModal"
      @mouseleave="isHovered=false"
    >
      <img 
        :src="'https://image.tmdb.org/t/p/w300'+movie.poster_path" class="card-img-top" 
        alt="" height="400px"
        >
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">
          {{movie.overview.substr(0, 100)}}...
        </p>
      </div>
    </div>
    
  </div>
</template>

<script>
// import axios from 'axios'

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
      console.log('MovieCard에서 감지')
    },
  },
}
</script>

<style>
.card {
  color: black;
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