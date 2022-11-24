<template>
  <div>
    <img class="background-img" :src="`https://source.unsplash.com/featured/?cinema`">
    <section class="section">
      <div class="section-right signup">
        <h1>로그인</h1>
        <form @submit.prevent="logIn" class="form">
          <label for="username">아이디 </label><br>
          <input type="text" id="username" v-model.trim="username">
          <!-- <span class="underline"></span> -->
          <br>
          <label for="password"> 비밀번호 </label><br>
          <input type="password" id="password" v-model.trim="password">
          <!-- <span class="underline"></span> -->
          <br>
          <input type="submit" value="로그인" class="btn btn-primary mt-5 mb-5"
            style="border-radius: 10px;"
            @click.prevent="logIn">
          <router-link :to="{ name: 'SignUpView' }" class="link" style="font-size: 1em;">아직 회원이 아니신가요? 회원가입하기</router-link>
        </form>
      </div>
    </section>
  </div>
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
      
      const userData = {
        username: username,
        password: password
      }

      if (!username) {
        alert('아이디는 필수예요!')
        return
      }
      if (!password) {
        alert('비밀번호는 필수예요!')
        return
      }

      console.log(userData)
      this.$store.dispatch('logIn', userData)
    },
  }
}
</script>

<style lang="scss">
#username, #id {
  margin-bottom: 3em;
}

.section {
  margin-top: 1em;
  max-height: 90vh;
  max-width: 50vw;
  margin: 3em auto;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  /* flex: 20%; */
  border-radius: $borderRadius+3;
  background-color: #191817;
  color: white;
  input {
    color: white;
    margin-bottom: 2em;
  }
}

.section-left {
  flex-basis: 40%;
  height: 100%;
  overflow: hidden;
  object-fit: none; /* Do not scale the image */
  object-position: center; /* Center the image within the element */
}

.section-right {
  /* flex-basis: 60%; */
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
  
}

.section-right form input {
  width: 100%;
  border: none;
  outline: none;
  border-bottom: 1px solid #BF93FF;
  margin-bottom: 1.2em;
  border-radius: 0;
  margin-bottom: 1.5em;
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