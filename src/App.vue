<template>
  <div id="app">
    <nav class="nav">
      <router-link :to="{ name: 'index' }">Movie</router-link> |
      <router-link :to="{ name: 'random' }">Random</router-link> |
      <router-link :to="{ name: 'watch' }">WatchList</router-link>
    </nav>
    <router-view />
  </div>
</template>


<script>
export default ({
  components: {
  },
  data() {
    return {
      videoUrl: null,
      isHovered: false,
    }
  },
})
</script>


<style>
* { padding:0;margin:0; box-sizing: border-box;}

body {
	padding: 0;
	margin: 0;
	height: 600vh;
	width: 100vw;
	font-family: "Nunito", sans-serif;
  /* position: relative; */
  background-color: #191817;
	/* background-color: #e34f37; */
	color: white;
}

ul,ol{list-style:none}
a{text-decoration:none;color:#fff;font-size:15px}

#app {
  font-family: 'Poppins', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

nav {
  position: sticky;
  top: 0;
  z-index: 1;
  padding: 30px;
  background-color: #21201E
}

nav a {
  font-weight: bold;
  color: white;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #914fce;
}
</style>
