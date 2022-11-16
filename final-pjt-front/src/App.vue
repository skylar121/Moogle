<template>
  <div id="app">
    <nav class="navbar navbar-dark bg-dark">
      <div class="container-fluid">
        <router-link :to="{ name: 'main' }"  class="navbar-brand">메인</router-link>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        </form>
        <router-link :to="{ name: 'SignUpView' }" class="text-white">회원가입</router-link> |
        <router-link :to="{ name: 'LogInView' }" class="text-white">로그인</router-link>
      </div>

      <!-- <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
        </ul>
      </div> -->
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


<style lang="scss">
* { padding:0;margin:0; box-sizing: border-box; text-decoration: none !important; color: #fff;}

a:hover {
  color: $primary !important;
}

body {
	padding: 0;
	margin: 0;
  position: relative;
  background-color: #191817;
}

ul,li,ol{list-style:none}
a{text-decoration:none;color:#fff;font-size:15px}

#app {
  font-family: 'Poppins', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
}

.nav {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 1;
  padding: 30px;
  background-color: #21201E;
}

.nav a {
  font-weight: bold;
  color: white;
  text-decoration: none;
}

.nav a.router-link-exact-active {
  color: $primary;
}

.logo {
  text-align: left;
}
</style>
