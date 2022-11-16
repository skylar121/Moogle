<template>
  <div class="p-5">
    <h3>보고싶은 날엔..눈물나는 날엔..</h3>
    <form @submit.prevent>
      <input @keyup.enter="addMovie" type="text" v-model="movieTitle">
      <input type="submit">
    </form>
    <div>
      <div v-for="(watchMovie, idx) in watchListMovie" :key="idx" @click="toggleClass(watchMovie)" :class="['cursor', watchMovie.completed? 'completed': null, watchListMovie.length%2? 'watch-list-odd' : 'watch-list-even']">
        {{watchMovie.title}}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WatchListView',
  data() {
    return {
      movieTitle: null,
      watchListMovie: [],
    }
  },
  computed: {
    watchListReverse() {
      const tmp = [...this.watchListMovie]
      tmp.reverse()
      return tmp
    }
  },
  methods: {
    addMovie() {
      const obj = {
        title: this.movieTitle,
        completed: false,
      }
      this.watchListMovie.unshift(obj)
      this.movieTitle = null
    },
    toggleClass(watchMovie) {
      watchMovie.completed = !watchMovie.completed
    }
  }
}
</script>

<style>
.completed {
  text-decoration: line-through;
}

.cursor {
  cursor: pointer;
}

.watch-list-even:nth-child(2n) {
  background-color: lightblue;
}

.watch-list-odd:nth-child(2n+1) {
  background-color: lightblue;
}

</style>