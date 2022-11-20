<template>
  <div class="container mb-3 p-4">
    <div>
      <form @submit.prevent="createReview" class="">
        <div class="star-box d-flex align-items-center justify-content-center mb-3">
          <b-form-rating
            id="rating-lg-no-border rating-inline"
            @change="onRate"
            :value="userReview[0].rank"
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
        <div v-if="!isEditing && userReview">
          <p>{{ userReview[0]?.title }}</p>
          <p>{{ userReview[0]?.content }}</p>
          <div class="d-flex justify-content-end">
            <button @click.prevent="onEdit" 
              type="submit" 
              class="btn btn-primary review-submit-btn"
            >
              별점 & 리뷰 수정 
              <i class="fa-solid fa-pen-to-square"></i>
            </button>
          </div>
        </div>
        <div v-else>
        <!-- <div> -->
          <div class="mb-3 review-input text-center" @change="onRate" >
            <label for="reviewTitle" class="form-label">제목</label>
            <input v-model="reviewTitle" class="form-control" id="reviewTitle" rows="3" placeholder="2자 이상 남겨주세요.">
          </div>
          <div class="mb-3 review-input" @change="onRate" >
            <label for="reviewContent" class="form-label">내용</label>
            <textarea v-model="reviewContent" class="form-control" id="reviewContent" rows="3" placeholder="2자 이상 남겨주세요.">{{}}</textarea>
          </div>

          <div v-if="!isEditing" class="d-flex justify-content-end">
            <button @click.prevent="createReview" type="submit" class="btn btn-primary review-submit-btn">별점 & 리뷰 저장 <i class="fa-solid fa-pen-to-square"></i></button>
            <button type="button" @click="onEdit()" class="btn btn-dark text-light">취소</button>
          </div>

          <div v-else class="d-flex justify-content-end">
            <button @click.prevent="updateReview" type="submit" class="btn btn-primary review-submit-btn">수정 완료 <i class="fa-solid fa-pen-to-square"></i></button>
            <button type="button" @click="onEdit()" class="btn btn-dark text-light">취소</button>
          </div>
        </div>
        <!-- <div class="mb-3 form-check review-check">
          <input type="checkbox" class="form-check-input" id="private">
          <label class="form-check-label me-2" for="private">비밀글</label>
          <span id="emailHelp" class="form-text text-muted">나만 볼 수 있어요.</span>
        </div> -->
        
      </form>
    </div>

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
      reviewTitle: this.userReview[0]?.title,
      reviewRating: this.propStar,
      reviewContent: this.userReview[0]?.content,
      isEditing: false,
    }
  },
  computed: {
    ...mapState([
      'token',
      'currUser'
    ]),
    ...mapGetters([
      'isLogin',
    ]),
  },
  methods: {
    onRate() {
      if (!this.isLogin) {
        console.log(this.isLogin)
        if (confirm('리뷰를 남기려면 로그인해주세요') == true){ 
          //true는 확인버튼을 눌렀을 때 코드 작성
          this.$router.push({name: 'LogInView'})
        }
      }
    },
    createReview() {
      if (!this.reviewRating || this.reviewRating <= 0.0 ) {
        alert('별점은 필수입니다!')
        this.reviewRating = null
        return
      }
      if (!this.reviewContent) {
        alert('제목은 필수입니다!')
        this.reviewContent = null
        return
      }
      if (!this.reviewContent) {
        alert('리뷰도 필수입니다!')
        this.reviewContent = null
        return
      }
      if (this.reviewContent.length < 2) {
        alert('보다 좋은 커뮤니티를 위해 2자 이상 작성 부탁드려요!')
        return
      }
      const reviewItem = {
        title: this.reviewTitle,
        content: this.reviewContent,
        rank: this.reviewRating,
        movie: this.movie.id
      }
      console.log(this.token)
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
    onEdit () {
      this.isEditing = !this.isEditing
    },
    updateReview() {
      if (!this.reviewRating || this.reviewRating <= 0.0 ) {
        alert('별점은 필수입니다!')
        this.reviewRating = null
        return
      }
      if (!this.reviewContent) {
        alert('제목은 필수입니다!')
        this.reviewContent = null
        return
      }
      if (!this.reviewContent) {
        alert('리뷰도 필수입니다!')
        this.reviewContent = null
        return
      }
      if (this.reviewContent.length < 2) {
        alert('보다 좋은 커뮤니티를 위해 2자 이상 작성 부탁드려요!')
        return
      }
      const reviewItem = {
        title: this.reviewTitle,
        content: this.reviewContent,
        rank: this.reviewRating,
        movie: this.movie.id
      }

      console.log(reviewItem)
      console.log((this.token))
      
      axios({
        method: 'put',
        url: api.movies.updateReview(this.movie.id),
        data: reviewItem,
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.isEditing = false
          this.$emit('fetchAllReviews')
          // this.reviewRating = null
          // this.reviewTitle = null
          // this.reviewContent = null
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.$emit('fetchAllReviews')
  }
}
</script>

<style>
/* 별 크기 키우기 */
#rating-lg-no-border\ rating-inline {
  font-size: 1.5rem;
}

#review {
  color: #dee2e6;
}

.review-input input {
  color: white;
  width: 100%;
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