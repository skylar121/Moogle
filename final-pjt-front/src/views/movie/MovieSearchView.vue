<template>
  <div>
    <div v-if="searchResults.length > 0">
      <div 
        v-for="(result, idx) in searchResults" :key="idx"
        @click="goToDetail(result.id)"
      >
        {{ result }}
        <hr>
      </div>
    </div>
    <div v-else>
        <p>검색 결과가 없습니다.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieSearch',
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

</style>