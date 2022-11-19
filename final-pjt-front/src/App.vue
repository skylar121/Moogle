<template>
  <div id="app">
    <nav>
      <div class="logo">
        <router-link :to="{ name: 'MainView' }">
          <span contenteditable>
            neon lights
          </span>
        </router-link>
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
    <router-link :to="{ name: 'DetailView' }"></router-link>
    <router-view />
  </div>
</template>


<script>
import { mapState } from 'vuex'

export default ({
  computed: {
    ...mapState([
      'isLogin',
    ])
  },
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
  font-family: 'Poppins', 'Noto Sans KR', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #fff;
}

a {
  text-decoration:none;
  color:#fff;
  cursor: pointer;
}

nav {
  overflow: hidden;
  padding: 3em;
  color: #fff;
  /* background-color:#21201E; */
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  /* align-items: center; */
  flex-wrap: wrap;
  position: sticky;
  top: 0;
  z-index: 1;
}

nav a {
  font-weight: bold;
  color: white;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: $primary;
}

input {
  height: 3em;
  border-radius: 10px;
}

.search {
  margin-top: -.4em;
  width: 30%;

}

.user-menu {

  .menu-items {
    color: white;
    margin-right: 1em;
  }
}

/* 로고 네온사인 */
:root {
  /* Set neon color */
  --neon-text-color: #bc13fe;
  --neon-border-color: rgb(0, 153, 255);
}

.logo a {

}

.logo span {
  font-size: 1.2rem;
  font-weight: 200;
  font-style: italic;
  color: #fff;
  padding: 1.2em 2em;
  border: 0.3rem solid #fff;
  border-radius: 2rem;
  text-transform: uppercase;
  animation: flicker 3s infinite alternate;
  ::-moz-selection {
    background-color: var(--neon-border-color);
    color: var(--neon-text-color);
  }
  ::selection {
    background-color: var(--neon-border-color);
    color: var(--neon-text-color);
  }
  :focus {
    outline: none;
  }
}

/* Animate neon flicker */
@keyframes flicker {
  0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
      
        text-shadow:
            -0.2rem -0.2rem 1rem #fff,
            0.2rem 0.2rem 1rem #fff,
            0 0 2rem var(--neon-text-color),
            0 0 4rem var(--neon-text-color),
            0 0 6rem var(--neon-text-color),
            0 0 8rem var(--neon-text-color),
            0 0 10rem var(--neon-text-color);
        
        box-shadow:
            0 0 .5rem #fff,
            inset 0 0 .5rem #fff,
            0 0 1.5rem var(--neon-border-color),
            inset 0 0 1.2rem var(--neon-border-color),
            0 0 1.5rem var(--neon-border-color),
            inset 0 0 .5rem var(--neon-border-color);        
    }
    
    20%, 24%, 55% {        
        text-shadow: none;
        box-shadow: none;
    }    
}
</style>
