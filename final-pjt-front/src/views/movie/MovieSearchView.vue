<template>
  <div>
    <div v-if="searchResults.length > 0">
      <div v-for="(result, idx) in searchResults" :key="idx">
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
  beforeRouteUpdate(to, from, next) {
    this.searchResults = to.params.searchResults
    next()
  }
}
</script>

<style>

</style>