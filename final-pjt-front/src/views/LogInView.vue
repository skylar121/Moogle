<template>
  <section class="section">
    <img class="section-left" :src="`https://source.unsplash.com/featured/?dessert`" alt="" width="300">
    <div class="section-right">
      <h1>로그인</h1>
      <form @submit.prevent="signUp" class="form">
        <label for="username">아이디 </label><br>
        <input type="text" id="username" v-model="username" required>
        <!-- <span class="underline"></span> -->
        <br>
        <label for="password1"> 비밀번호 </label><br>
        <input type="password" id="password1" v-model="password1" required minlength="8">
        <!-- <span class="underline"></span> -->
        <br>
        <label for="password2"> 비밀번호 확인 </label><br>
        <input type="password" id="password2" v-model="password2" required minlength="8">
        <!-- <span class="underline"></span> -->
        <br>
        <input type="submit" value="로그인" class="btn btn-primary">
        <router-link :to="{ name: 'SignUpView' }" class="link">아직 회원이 아니신가요? 회원가입하기</router-link>
      </form>
    </div>
  </section>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      
      const payload = {
        username: username,
        password: password
      }
      this.$store.dispatch('logIn', payload)
    },
  }
}
</script>

<style>
.section {
  width: 80%;
  height: 600px;
  background-color: white;
  color: black;
  margin: 5em auto;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  flex: 20%;
}

.section-left {
  flex-basis: 40%;
  height: 100%;
  overflow: hidden;
  object-fit: none; /* Do not scale the image */
  object-position: center; /* Center the image within the element */
}

.section-right {
  height: 100%;
  flex-basis: 60%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  margin: 0 auto;
  
}
.section-right h1 {
  margin: 1em auto;
}

.section-right form {
  width: 50%;
  margin: 3em auto;
  text-align: left;
  position: relative;
}

.section-right form input {
  width: 100%;
  border-bottom: 1px solid #BF93FF;
  outline: none;
  margin-bottom: 1.2em;
}

.link {
  display: block;
  text-align: center;
  font-size: .8rem;
  margin-top: -.8em;
}


/* input::-webkit-input-placeholder {
  color: #AAA;
}

input:focus::-webkit-input-placeholder {
  color: dodgerblue;
}

.section-right form input:focus+.underline {
  transform: scale(1);
}

.section-right form a {
  color: #000;
  text-align: center;
}

.underline {
  position: absolute;
  background-color: dodgerblue;
  display: inline-block;
  height: 2px;
  top: 185px;
  left: 50px;
  margin-top: -4px;
  -webkit-transform: scale(0, 1);
  transform: scale(0, 1);
  -webkit-transition: all 0.5s linear;
  transition: all 0.5s linear;
  width: 202px;
} */
</style>