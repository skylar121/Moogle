<template>
  <div>
    <div class="modal" 
      :style="{'display': isHovered? 'block': 'none'}" 
      @show-modal="showModal"
      @mouseleave="isHovered=false"
    >
      <p>{{videoUrl}}</p>
    </div>
    <div class="">
      <div class="">
        <MovieCard
          v-for="movie in movieData"
          :key="movie.id"
          :movie="movie"
          class=""
          @show-modal="showModal"
          />
      </div>
    </div>
  </div>

</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieView',
  components: {
    MovieCard,
  },
  data() {
    return {
      videoUrl: null,
      isHovered: false,
    }
  },
  methods:{
    showModal(isHovered, videoUrl) {
      this.videoUrl = videoUrl
      this.isHovered = isHovered
    },
  },
  computed: {
    movieData() {
      return this.$store.state.movieData
    }
  },
  created() {
    if (this.$store.state.movieData === null) {
      this.$store.dispatch('fetchMovie')
    }
  },
}
</script>

<style>
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