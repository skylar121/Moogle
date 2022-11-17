<template>
  <div id="app">
    <nav>
      <div class="logo">
        <router-link :to="{ name: 'main' }"  class="navbar-brand">로고</router-link>
      </div>
      <form class="search" role="search" @submit.prevent="showSearchPage">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" autocomplete="">
      </form>
      <div v-if="!isLogin" class="user-menu">
        <router-link :to="{ name: 'SignUpView' }" class="menu-items"><i class="fa-solid fa-user-plus fa-lg"></i></router-link>
        <router-link :to="{ name: 'LogInView' }" class="menu-items"><i class="fa-solid fa-right-to-bracket fa-lg"></i></router-link>
      </div>
      <div v-else>
        <router-link :to="{ name: 'MyPageView' }" class="menu-items">My Page</router-link>
        <span @click="logout">
          <i class="fa-solid fa-right-to-bracket fa-lg"></i>
        </span>
      </div>
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
  computed: {
    isLogin() {
      return this.$store.state.isLogin
    }
  },
  methods: {
    logout() {
      this.$store.commit('logout')
    },
  }
})
</script>


<style lang="scss">
* { padding:0; margin:0; box-sizing: border-box; text-decoration: none !important; transition: all 0.3s ease 0s !important;}

a:hover {
  color: $primary !important;
}

body {
	padding: 0;
	margin: 0;
  position: relative;
  background-color: $body-bg;
  color: #fff;
}

ul,li,ol{list-style:none}


#app {
  font-family: 'Poppins', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #fff;
}

a {
  text-decoration:none;
  color:#fff;
  font-size:15px;
  cursor: pointer;
}

nav {
  overflow:hidden;
  height: 80px;
  color: #fff;
  background-color:#21201E;
  margin:0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  position: sticky;
  top: 0;
  z-index: 1;
  padding: 30px;
}

.nav a {
  font-weight: bold;
  color: white;
  text-decoration: none;
}

.nav a.router-link-exact-active {
  color: $primary;
}

.user-menu {

  .menu-items {
    color: white;
    margin-right: 1em;
  }
}
</style>
