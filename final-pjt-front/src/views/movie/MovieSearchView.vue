<template>
  <div class="search-result">
    <p class="result"><span class="result-span">{{ this.$store.state.saveSearch }}</span>에 대한 검색 결과입니다.</p>
        <!-- <v-hover 
          v-slot="{ hover }"
          open-delay="200"
        > -->
      <v-row v-if="searchResults.length > 0">
        <v-col
          v-for="result in searchResults"
          :key="result.id"
          cols="3"
          class="poster-parent"
        >
          <!-- <v-expand-transition>
        <div
            v-if="hover"
            class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal text-h2 white--text"
            style="height: 10%;"
          >
            {{ result.title }}
          </div>
            </v-expand-transition> -->
            <!-- <div class="overlay">
              text
            </div> -->
            <v-img
              :src="result.poster_path? 'https://image.tmdb.org/t/p/original' + result.poster_path : 'https://image.tmdb.org/t/p/original' + result.backdrop_path" class="poster"
              @click="goToDetail(result.id)"
              id="search-card"
            >
            <!-- <p :class="hover ? 'hovering' : 'non-hovering'">환율</p> -->
              <template v-slot:placeholder>
                <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
                >
                  <v-progress-circular
                    indeterminate
                    color="grey lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>
        </v-col>
      </v-row>
    <p v-else class="result">검색 결과가 없습니다.</p>
        <!-- </v-hover> -->
  </div>
</template>

<script>
export default {
  name: 'MovieSearchView',
  props: {
    query: String,
  },
  data() {
    return {
      isHovering: false
    }
  },
  computed: {
    searchResults: {
      set: function () {
      },
      get: function () {
        return this.$store.state.searchResults
      }
    } 
  },
  methods: {
    goToDetail(id) {
      // console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: id }})
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.searchResults = to.params.searchResults
    next()
  },
  created() {
    console.log(this.query)
  }
}
</script>

<style>

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
/* .poster {
  justify-self: center;
  object-fit: cover;
}

.cstyle {
  position: relative;
  width: 100%;
  height: 0;
  overflow: hidden;
  padding-bottom: 150%;
}

.poster-parent {
  position: relative;
}

.hovering {
  opacity: 0.8;
  color: black;
  width: 50%;
  bottom: 0;
  position: absolute;
  z-index: 3;
  text-align: center;
  left: 50%;
  transform: translateX(-50%);
  font-weight: 600;
}

.non-hovering {
  display: none;
} */

.result {
  text-align: center;
  font-weight: 600;
  font-size: 4vw;
  margin-bottom: 6%;
  margin-top: -2%;
}

.result-span {
  color: orange;
}
</style>