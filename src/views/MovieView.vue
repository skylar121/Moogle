<template>
  <div>
    <!-- 마우스오버시 디테일 -->
    <div class="modal" :style="{ 'display': isHovered ? 'block' : 'none' }" @show-modal="showModal"
      @mouseleave="isHovered = false">
      <p>{{ videoUrl }}</p>
    </div>

    <div class="row-title">
      TOP RATED
    </div>

    <carousel-3d 
      v-if="movieData" 
      :controls-visible="true" 
      :inverse-scaling="200" 
      :disable3d="false" 
      :space="450" :display="9" 
      :height="550" 
      @mouseenter="showModal" 
      autoplay 
    >
      <slide v-for="(movie, idx) in movieData" :key="movie.id" :index="idx">
        <!-- <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }"> -->
        <template slot-scope="{ index }" >
          <router-link :to="{ name: 'movieDetail', params: { id: movie.id } }">
            <div class="movie-item" :data-index="index" @show-modal="showModal">
              <!-- <img  :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="'https://image.tmdb.org/t/p/original'+movie.poster_path" > -->
              <img :src="'https://image.tmdb.org/t/p/original' + movie.poster_path" :height="500">
              <span class="movie-title">{{ movie.title }}</span>
            </div>
          </router-link>
        </template>
      </slide>
    </carousel-3d>
  </div>

</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'MovieView',
  components: {
    Carousel3d,
    Slide,
  },
  data() {
    return {
      videoUrl: null,
      isHovered: false,
    }
  },
  methods: {
    showModal(movie) {
      this.videoUrl = `https://www.youtube.com/results?search_query=${movie.title} 공식 예고편`
      this.isHovered = true
      console.log('카드 마우스오버');
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
  mounted() {
  }
}
</script>

<style lang="scss">
.carousel-3d-container {

  .carousel-3d-slider {
    background: unset;
  }

  .carousel-3d-slide {
    background: unset;
    border: none;

    .movie-item {
      position: relative;
      cursor: pointer;
      transition: all 0.5s;
      -moz-transition: all 0.5s;
      -webkit-transition: all 0.5s;
      -o-transition: all 0.5s;
      text-decoration: none;
    }
    
    .movie-title {
      position: absolute;
      width: 80%;
      left: 50%;
      bottom: -3em;
      transform: translate(-50%, -50%);
      /* backdrop-filter: blur(4px); */
      /* line-height: 70px; */
      border-radius: 10px;
      text-align: center;
      text-decoration: none;
    }
    .movie-item:hover{
    }
  }
}

.row-title {
  font-size: 1.5rem;
  font-weight: 800;
  margin-top: 1em;
}

</style>