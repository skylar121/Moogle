<template>
  <div>
    <div class="modal" 
      :style="{'display': isHovered? 'block': 'none'}" 
      @show-modal="showModal"
      @mouseleave="isHovered=false"
    >
      <p>{{videoUrl}}</p>
    </div>
    <div class="slider-section">
      <div class="wheel">
        <MovieCard
          v-for="movie in movieData"
          :key="movie.id"
          :movie="movie"
          class="wheel-card"
          @show-modal="showModal"
          />
      </div>
    </div>
    <carousel-3d :space="350" :display="5">
      <slide 
        v-for="(movie, idx) in movieData"
        :key="movie.id" :index="idx">
          <template slot-scope="{ index, isCurrent, leftIndex, rightIndex }">
            <img :data-index="index" :class="{ current: isCurrent, onLeft: (leftIndex >= 0), onRight: (rightIndex >= 0) }" :src="'https://image.tmdb.org/t/p/original'+movie.poster_path" >
        </template>
      </slide>
    </carousel-3d>
    <div class="scroll-down">Scroll down<div class="arrow"></div>
</div>
  </div>

</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'
// import gsap from 'gsap'
// import { Flip } from 'gsap/Flip'
// import ScrollTrigger from "gsap/ScrollTrigger"
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieView',
  components: {
    Carousel3d,
    Slide,
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
    // spinner() {
    //   gsap.registerPlugin(ScrollTrigger)
    //   let wheel = document.querySelector(".wheel");
    //   let images = gsap.utils.toArray(".wheel__card");

    //   gsap.to(".arrow", { y: 5, ease: "power1.inOut", repeat: -1, yoyo: true });
    //   function gsapSetup() {
    //     let radius = wheel.offsetWidth / 2;
    //     let center = wheel.offsetWidth / 2;
    //     let total = images.length;
    //     let slice = (2 * Math.PI) / total;

    //     images.forEach((item, i) => {
    //       let angle = i * slice;

    //       let x = center + radius * Math.sin(angle);
    //       let y = center - radius * Math.cos(angle);

    //       gsap.set(item, {
    //         rotation: angle + "_rad",
    //         xPercent: -50,
    //         yPercent: -50,
    //         x: x,
    //         y: y
    //       });
    //     });
    //   }

    //   gsapSetup()

    //   window.addEventListener("resize", gsapSetup);

    //   gsap.to(".wheel", {
    //     rotate: () => -360,
    //     ease: "none",
    //     duration: images.length,
    //     scrollTrigger: {
    //       start: 0,
    //       end: "max",
    //       scrub: 1,
    //       snap: 1 / images.length,
    //       invalidateOnRefresh: true
    //     }
    //   });

    //   let cards = gsap.utils.toArray(".wheel__card");
    //   let header = document.querySelector(".header");
    //   // let body = document.querySelector(".header");

    //   // let isFullScreen = false;

    //   // keep track of last clicked card so we can put it back
    //   let lastClickedCard;

    //   cards.forEach((card) => {
    //     card.addEventListener("click", (e) => {
    //       if (lastClickedCard) {
    //         putBack(e);
    //       }
    //       flip(e);
    //     });
    //   });

    //   header.addEventListener("click", (e) => {
    //     if (!lastClickedCard) return;
    //     putBack(e);
    //   });

    //   function putBack() {
    //     let image = header.querySelector("img");

    //     let state = Flip.getState(image);

    //     lastClickedCard.appendChild(image);

    //     Flip.from(state, {
    //       duration: 0.6,
    //       ease: "sine.out",
    //       absolute: true
    //     });

    //     lastClickedCard = null;
    //   }

    //   function flip(e) {
    //     let image = e.target.querySelector("img");

    //     let state = Flip.getState(image);

    //     header.appendChild(image);

    //     Flip.from(state, {
    //       duration: 0.6,
    //       ease: "sine.out",
    //       absolute: true
    //     });

    //     lastClickedCard = e.target;
    //   }
    // }
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
    // this.spinner()
  }
}
</script>

<style>
/* .slider-section {
	height: 22vh;
	bottom: 0;
	position: fixed;
	width: 100%;
}

.wheel {
	position: absolute;
	top: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	width: 300vw;
	height: 300vw;
	max-width: 2000px;
	max-height: 2000px;
	left: 50%;
	transform: translateX(-50%);
}

.wheel__card {
	position: absolute;
	top: 0;
	left: 0;
	width: 6%;
	max-width: 200px;
	aspect-ratio: 1 / 1;
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
} */
</style>