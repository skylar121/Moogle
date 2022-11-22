<template>
  <div>
        <v-hover 
          v-slot="{ hover }"
          open-delay="200"
        >
    <v-row>
      <v-col
        v-for="result in searchResults"
        :key="result.id"
        cols="3"
        class="poster-parent"
      >
         <v-expand-transition>
        <div
            v-if="hover"
            class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal text-h2 white--text"
            style="height: 10%;"
          >
            {{ result.title }}
          </div>
           </v-expand-transition>
          <v-img
            :src="result.poster_path? 'https://image.tmdb.org/t/p/original' + result.poster_path : 'https://image.tmdb.org/t/p/original' + result.backdrop_path" class="poster"
            @click="goToDetail(result.id)"
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
        </v-hover>
  </div>
</template>

<script>
export default {
  name: 'MovieSearch',
  data() {
    return {
      isHovering: false
    }
  },
  computed: {
    searchResults(){
      return this.$store.state.searchResults
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
  }
}
</script>

<style>
.poster {
  justify-self: center;
  object-fit: cover;
}

.cstyle {
  position: relative;
  width: 100%;
  /* height: 0; */
  overflow: hidden;
  padding-bottom: 150%;
}

.poster-parent {
  position: relative;
}

.hovering {
  background-color: white;
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
}
</style>