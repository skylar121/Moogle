<template>
  <div class="container" >
    <div class="text-center mt-3">
      <h3 class="fw-bold fs-2" >MY REVIEW</h3>
    </div>
    <form @submit.prevent="createReview">
      <div class="star-box d-flex align-items-center justify-content-center mb-3">
        <!-- 유저 리뷰가 있다면 -->
        <div v-if="userReview">
          <b-form-rating
            id="rating-lg-no-border rating-inline"
            @change="onRate"
            :value="userReview?.[0]?.rank"
            icon-half="star-half"
            variant="danger"
            no-border inline show-value show-clear
            precision="1"
            class="star text-light w-100"
            size="lg"
            color="#ffd21e"
          ></b-form-rating>
        </div>
        <!-- 유저 리뷰가 없다면 -->
        <div v-else>
          <b-form-rating
            id="rating-lg-no-border rating-inline"
            @change="onRate"
            v-model="reviewRating"
            icon-half="star-half"
            variant="danger"
            no-border inline show-value show-clear
            precision="1"
            class="star text-light w-100"
            size="lg"
            color="#ffd21e"
          ></b-form-rating>
        </div>
      </div>

      <!-- 수정중 X & 리뷰 있다면 내용 + 수정 + 삭제 버튼 보여주기 -->
      <div v-if="(!isEditing && userReview && userReview?.length > 0)" class="text-center">
        <p class="fs-3">{{ userReview?.[0]?.title }}</p>
        <p style="color: #999;">{{ userReview?.[0]?.content }}</p>
        <div>
          <!-- 수정 -->
          <button @click="onEdit" 
            class="btn btn-primary review-submit-btn me-2"
          >
            <i class="fa-solid fa-pen-to-square"></i>
          </button>
          <!-- 삭제 -->
          <button @click.prevent="deleteReview" 
            type="submit" 
            class="btn review-submit-btn"
            style="color: #999;"
          >
          <i class="fa-solid fa-trash-can" style="cursor: pointer"></i>
          </button>
        </div>
      </div>

      <!-- 수정중 OR 리뷰 없다면 리뷰 form -->
      <div v-else class="w-75 my-0 mx-auto">
        <!-- 리뷰 있다면 UPDATE -->
        <div v-if="isEditing && userReview && userReview?.length > 0">
          <div class="mb-3 review-input text-center" @change="onRate" >
            <label for="reviewTitle" class="form-label">제목</label>
            <input 
              :value="reviewTitle" 
              class="" id="reviewTitle" rows="3" 
              placeholder="2자 이상 남겨주세요." 
            >
          </div>
          <div class="mb-3 review-input" @change="onRate" >
            <label for="reviewContent" class="form-label">내용</label>
            <textarea v-model="reviewContent" class="" id="reviewContent" rows="3" placeholder="2자 이상 남겨주세요."></textarea>
          </div>
          <div class="d-flex justify-content-end">
            <!-- 수정 완료 -->
            <button @click.prevent="updateReview" type="submit" class="btn btn-primary review-submit-btn me-2"> 
              <!-- 저장  -->
              <i class="fa-solid fa-floppy-disk"></i></button>
            <!-- 수정 취소 -->
            <button type="button" @click="onEdit" class="btn btn-dark text-light">
              <!-- 취소 -->
              <i class="fa-solid fa-xmark"></i></button>
          </div>
        </div>
        <!-- 리뷰 없다면 CREATE -->
        <div v-else class="-flex flex-column justify-content-end align-items-center">            
          <div class="mb-3 review-input text-center" @change="onRate">
            <label for="reviewTitle" class="form-label fs-4">제목</label>
            <input v-model="reviewTitle" class="" id="reviewTitle" rows="3" placeholder="2자 이상 남겨주세요.">
          </div>
          <div class="mb-3 review-input text-center" @change="onRate">
            <label for="reviewContent" class="form-label fs-5">내용</label>
            <div class="d-block w-100"><textarea v-model="reviewContent" id="reviewContent" rows="3" placeholder="2자 이상 남겨주세요.">{{}}</textarea></div>
          </div>
          <div class="d-flex justify-content-end">
            <!-- 별점 & 리뷰 저장 -->
            <button @click.prevent="createReview" type="submit" class="btn btn-primary review-submit-btn"><i class="fa-solid fa-floppy-disk"></i></button>
          </div>
        </div>
      </div>
      <!-- <div class="mb-3 form-check review-check">
        <input type="checkbox" class="form-check-input" id="private">
        <label class="form-check-label me-2" for="private">비밀글</label>
        <span id="emailHelp" class="form-text text-muted">나만 볼 수 있어요.</span>
      </div> -->
      
    </form>

    <!-- 이전 화면으로 돌아갈수 있다면... -->
    <!-- <div v-else class="my-3">
      <button type="button" class="btn btn-outline-primary">
        <router-link :to="{ name: 'LogInView' }" class="">
        별점 & 리뷰를 남기려면 로그인하러 가기 🐱
        </router-link>
      </button>
    </div> -->

  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapGetters } from 'vuex'
import { BFormRating } from 'bootstrap-vue'
import api from '@/api/api'

export default {
  name: 'MovieCreateReview',
  components: {
    BFormRating
  },
  props: {
    userReview: Array,
    propStar: Number,
    movie: Object,
  },
  data() {
    return {
      isEditing: false,
    }
  },
  computed: {
    ...mapState([
      'token',
    ]),
    ...mapGetters([
      'isLogin'
    ]),

    reviewTitle() {
      return this.userReview?.[0]?.title
    },
    reviewContent() {
      return this.userReview? this.userReview?.[0]?.content : null
    },
    reviewRating() {
      return this.userReview? this.userReview?.[0]?.rank : this.propStar
    },
  },
  // reviewTitle: {
  //   get() {
  //     return this.userReview?.[0]?.title
  //   },
  //   set(newTitle) {
  //     this.userReview.title = newTitle
  //   }
  // },
  // reviewContent: {
  //   get() {
  //     return this.userReview? this.userReview?.[0]?.content : null
  //     return this.userReview? this.userReview?.[0]?.content : null
  //   },
  //   set(newContent) {
  //     this.userReview.content = newContent
  //   }
  // },
  // reviewRating: {
  //   get() {
  //     return this.userReview? this.userReview?.[0]?.rank : this.propStar
  //   },
  //   set(newRank) {
  //     this.userReview.rank = newRank
  //   }
  methods: {
    onRate() {
      if (!this.isLogin) {
        console.log(this.isLogin)
        if (confirm('리뷰를 남기려면 로그인해주세요.') === true){ 
          this.reviewRating = null
          this.$router.push({name: 'LogInView'})
        }
      }
    },
    createReview() {
      const title = document.querySelector('#reviewTitle').value
      const content = document.querySelector('#reviewContent').value
      const rank = document.querySelector("#rating-lg-no-border\\ rating-inline").getAttribute("aria-valuenow")
      if (!rank || rank <= 0.0 ) {
        alert('별점은 필수입니다!')
        return
      }
      if (!title) {
        alert('제목은 필수입니다!')
        return
      }
      if (!content) {
        alert('리뷰도 필수입니다!')
        return
      }
      if (title?.length < 2 || content?.length < 2) {
        alert('2자 이상 작성해주세요 :)')
        return
      }
      const reviewItem = {
        title, 
        content, 
        rank,
        movie: this.movie.id
      }
      // console.log(this.movie.id)
      axios({
        method: 'post',
        url: api.movies.createReview(this.movie.id),
        data: reviewItem,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.$emit('fetchAllReviews')
          // this.reviewRating = null
          // this.reviewTitle = null
          // this.reviewContent = null
        })
        .catch((err) => {
          console.log(err)
        })
    },
    onEdit() {
      this.isEditing = !this.isEditing
      console.log(this.isEditing)
    },
    updateReview() {
      if (!this?.reviewRating || this?.reviewRating <= 0.0 ) {
        alert('별점은 필수입니다!')
        this.reviewRating = null
        return
      }
      if (!this.reviewTitle) {
        alert('제목은 필수입니다!')
        this.reviewTitle = null
        return
      }
      if (this.reviewTitle?.length < 2) {
        alert('2자 이상 작성해주세요 :)')
        return
      }
      if (!this.reviewContent) {
        alert('리뷰도 필수입니다!')
        this.reviewContent = null
        return
      }
      if (this.reviewContent?.length < 2) {
        alert('2자 이상 작성해주세요 :)')
        return
      }
      const title = document.querySelector('#reviewTitle').value
      const content = document.querySelector('#reviewContent').value
      const rank = document.querySelector("#rating-lg-no-border\\ rating-inline").getAttribute("aria-valuenow")
      // console.log(rank)
      const reviewItem = {
        title, content, rank
      }
      // console.log((this.token))
      // console.log(this.userReview[0])
      // console.log(api.movies.updateReview(this.userReview[0].id))
      axios({
        method: 'put',
        url: api.movies.updateDeleteReview(this.userReview[0].id),
        data: reviewItem,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then(() => {
          // console.log(res)
          this.isEditing = false
          this.$emit('fetchAllReviews')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview() {
      if (confirm('진짜 삭제할까요?') === true) {
        axios({
          method: 'delete',
          url: api.movies.updateDeleteReview(this.userReview[0].id),
          headers: {
            Authorization: `Token ${this.token}`
          }
        })
          .then(() => {
            // console.log(res)
            alert('정상적으로 삭제되었어요.')
            this.isEditing = false
            this.$emit('fetchAllReviews')
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  },
  created() {
    this.$emit('fetchAllReviews')
  }
}
</script>

<style lang="scss">
/* 별 크기 키우기 */
#rating-lg-no-border\ rating-inline {
  font-size: 1.5rem;
}

/* #review {
  color: #dee2e6;
} */

textarea {
  width: 100%;
  height: 6.25em;
  border: none;
  resize: none;
}

#reviewTitle, #reviewContent {
  /* outline: none; */
  border: none;
  border-bottom: 1px solid $primary;
  color: white;
  border-radius: 0;
}

.review-input input {
  color: white;
  width: 100%;
  border: none;
  outline: none;
  border-bottom: 1px solid #BF93FF;
  outline: none;
  margin-bottom: 1.2em;
}

.review-check input {
  border: 1px solid white;
}

.review-submit-btn {
  /* position: absolute;
  bottom: -4em; */
  right: 0;
}

</style>