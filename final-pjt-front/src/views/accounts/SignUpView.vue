<template>
  <div>
    <img class="background-img" :src="`https://source.unsplash.com/featured/?cinema`">
    <section class="section">
      <img class="section-left" :src="`https://source.unsplash.com/featured/?cinema`" alt="" width="300">
      <div class="section-right">
        <h1>회원가입</h1>
        <form @submit.prevent="signUp" class="form">
          <label for="id">아이디 </label><br>
          <input type="text" id="id" v-model="id" required  minlength="2" maxlength="12">
          <br>
          <label for="nickname">닉네임 </label><br>
          <input type="text" id="nickname" v-model="nickname" required minlength="2" maxlength="10">
          <br>
          <label for="password1"> 비밀번호 </label><br>
          <input type="password" id="password1" v-model="password1" required minlength="8">
          <br>
          <label for="password2"> 비밀번호 확인 </label><br>
          <input type="password" id="password2" v-model="password2" required minlength="8">
          <br>
          <label for="profileImg" class="form-label">프로필 이미지 업로드</label>
          <v-file-input accept="image/*" type="file" id="profileImg" @change="selectFile"></v-file-input>
          <!-- <input accept="image/*" type="file" ref="profileImg" @change="selectFile"> -->
          <br>
          <input type="submit" value="회원가입"  class="btn btn-primary" @click.prevent="signUp">
          <router-link :to="{ name: 'LogInView' }" class="link">이미 회원이신가요? 로그인하기</router-link>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      id: null,
      nickname: null,
      password1: null,
      password2: null,
      profile_image: null,
    }
  },
  methods: {
    selectFile(file) {
      console.log(file)
      this.profile_image = file
    },
    // selectFile() {
    //   // this.profile_image = file
    //   console.log(this.$refs.profileImg)
    //   this.profile_image = this.$refs.profileImg.file
    // },
    signUp() {
      const id = this.id
      const nickname = this.nickname
      const password1 = this.password1
      const password2 = this.password2
      const profile_image = this.profile_image
      // js 축약문법 (key, value 이름 같을 경우)
      // const payload = {
      //   id, password1, password2
      // }
      if (!id) {
        alert('아이디는 필수입니다.')
        return
      }
      if (!nickname) {
        alert('닉네임은 필수입니다.')
        return
      }
      if (!password1) {
        alert('비밀번호는 필수입니다.')
        return
      }
      if (password1 != password2) {
        alert('비밀번호가 일치하지 않습니다.')
        this.password1 = null
        this.password2 = null
        return
      } else if (!profile_image) {
        alert('사진은 필수예요ㅠㅠ')
        return
      } else {
        const userData = {
          id: id, 
          nickname: nickname, 
          password1: password1, 
          password2: password2,
          profile_image: profile_image,
        }
        console.log(userData)
        this.$store.dispatch('signUp', userData)
      }
    }
  }
}
</script>

<style lang="scss">
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
  border-radius: $borderRadius+3;
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
}

.section-right form input {
  width: 100%;
  border-bottom: 1px solid #BF93FF;
  outline: none;
  margin-bottom: 1.2em;
}

.link {
  display: block;
  text-align:center;
  font-size: .8rem;
  margin-top: -.8em;
}

// .link:hover {
//   color: orange;
// }

</style>