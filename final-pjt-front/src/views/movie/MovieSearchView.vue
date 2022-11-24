<template>
  <div class="search-result">
    <v-row v-if="searchResults?.length > 0">
      <p class="result">
        <span class="result-span text-primary">{{ this.$store.state.saveSearch }}</span
        >에 대한 검색 결과
      </p>
      <v-col
        v-for="result in searchResults"
        :key="result.id"
        cols="3"
        class="poster-parent"
      >
        <v-img
          :src="
            result.poster_path
              ? 'https://image.tmdb.org/t/p/original' + result.poster_path
              : 'https://image.tmdb.org/t/p/original' + result.backdrop_path
          "
          class="poster"
          @click="goToDetail(result.id)"
          id="search-card"
          @mouseover="isHovering = result.id"
          @mouseleave="isHovering = null"
          height="25vw"
          object-fit="cover"
        >
          <template v-slot:placeholder>
            <v-row class="fill-height ma-0" align="center" justify="center">
              <v-progress-circular
                indeterminate
                color="grey lighten-5"
              ></v-progress-circular>
            </v-row>
          </template>
        </v-img>
        <p @mouseover="isHovering = result.id" v-show="isHovering === result.id" class="hovering">{{ result.title }}</p>
      </v-col>
    </v-row>
    <p v-else class="result">검색 결과가 없습니다 😿</p>
    <!-- </v-hover> -->
  </div>
</template>

<script>
export default {
  name: "MovieSearchView",
  props: {
    query: String,
  },
  data() {
    return {
      isHovering: false,
    };
  },
  computed: {
    searchResults: {
      set: function () {},
      get: function () {
        return this.$store.state.searchResults;
      },
    },
  },
  methods: {
    goToDetail(id) {
      // console.log('클릭', id)
      this.$router.push({ name: "DetailView", params: { movie_id: id } });
    },
  },
  beforeRouteUpdate(to, from, next) {
    this.searchResults = to.params.searchResults;
    next();
  }
};
</script>

<style lang="scss">
.overlay {
  padding: 15px 20px;
  background-color: #444444;
  border-radius: 5px;
  color: #ffffff;
  position: absolute;
  opacity: 0;
  transition: all ease 0.5s;
  z-index: 2;
}
#search-card:hover + .overlay {
  opacity: 1;
}

.search-result {
  justify-self: center;
  position: absolute;
  width: 80%;
  left: 50%;
  transform: translateX(-50%);
  margin-top: 3%;
}

.hovering {
  z-index: 3;
  position: absolute;
  margin-top: -19%;
  margin-left: 5.7%;
  font-weight: 600;
  background-color: rgb(0, 0, 0, 0.5);
  width: 10vw;
  text-align: center;
  word-break: keep-all;
  color: $primary;
}

/* .hovering {
  position: absolute;
  z-index: 3;
  bottom: 0;
  left: 10%;
  backdrop-filter: blur(8px);
  border-bottom: 2px solid $primary;
  text-align: center;
  text-decoration: none;
  min-height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  white-space: nowrap;
  padding: .4em;
  overflow: hidden;
} */

.result {
  text-align: center;
  font-weight: 600;
  font-size: 2em;
  margin-bottom: 1em;
  margin-top: .5em;
}

</style>