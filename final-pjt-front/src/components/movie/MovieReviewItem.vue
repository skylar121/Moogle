<template>
  <div @click="goToReviewDetail" class="card review-card">
    <div class="card-header text-bg-primary d-flex justify-content-between align-items-center">
      <strong>{{ review.nickname }}</strong>
      <div>
        <button v-if="currUser.username !== review.username"  @click="goToProfile" class="btn">프로필 보기</button>
        <button v-if="currUser.username === review.username" @click="deleteReview" class="btn"><i class="fa-solid fa-trash-can" style="cursor: pointer"></i></button>
      </div>
    </div>
    <div class="card-body d-flex flex-column justify-content-center align-items-center">
      <p class="card-title fs-3">{{ review.title }}</p>
      <p v-if="review.content.length > 50" class="card-text text-muted">{{ `${review.content.slice(0,50)} ...더보기` }}</p>
      <p v-else>{{review.content}}</p>
      <div class="movieVoteAverage">
        <b-form-rating
          :value="review.rank"
          readonly
          show-value
          precision="1"
          color="#ffd21e"
          class="border-0 text-light"
        ></b-form-rating>
        <!-- <p>{{ movie?.vote_average.toFixed(1) > 0.0 ? `⭐${movie?.vote_average.toFixed(1)} / 10` : '아직 별점이 없어요!' }} </p> -->
      </div>
      <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
    </div>
    <div class="card-footer text-muted d-flex justify-content-between">
      <div class="fs-5">
        <span v-if="!initialHeart">
          <i class="fa-regular fa-heart me-2" id="toggleLike" @click="toggleLike"></i>
        </span>
        <span v-else>
          <i class="fa-solid fa-heart me-2" id="toggleLike" @click="toggleLike"> </i>
        </span>
        <span class="me-2">{{ likeCount }}</span>
        <i class="fa-regular fa-comment" style="cursor: pointer"></i>
        <span class="me-2">댓글 보기</span>
        <MovieCommentItem />
        <div>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Launch demo modal
    </button>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            ...
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
      </div>
      {{ review.updated_at.slice(0, 10) }}
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import api from '@/api/api'
// import MovieCommentItem from '@/components/movie/MovieCommentItem'

import { mapState } from 'vuex'
export default {
  name: 'MovieReviewItem',
  data() {
    return {
      likeCount: null,
      // msg: null,
      initialHeart: false,
    }
  },
  components: {
    // MovieCommentItem,
  },
  props: {
    review: Object,
  },
  computed: {
    ...mapState([
      'token',
      'currUser'
    ]),
  },
  methods: {
    toggleLike() {
      axios({
        method: 'get',
        url: api.movies.toggleReviewLike(this.review.id),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.likeCount = res.data.like_count
          // this.msg = res.data.message
          this.initialHeart = !this.initialHeart
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getLikeCount() {
      axios({
        method: 'get',
        url: api.movies.getReviewCount(this.review.id),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          // console.log('댓글정보')
          // console.log(res.data)
          this.likeCount = res.data.like.length
          if (res.data.like !== [] && res.data.like.includes(this.currUser.id)) {
            this.initialHeart = true
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteReview() {
      console.log('삭제해줘')
      console.log(this.review)
      if (confirm('진짜 삭제할까요?') === true) {
        axios({
          method: 'delete',
          url: api.movies.updateDeleteReview(this.review.id),
          headers: {
            Authorization: `Token ${this.token}`
          }
        })
          .then(() => {
            // console.log(res)
            alert('정상적으로 삭제되었어요.')
            this.isEditing = false
            // 새로고침 안해도 알아서 재렌더링되게 수정해야함..
            // this.$router.go()
            this.$emit('fetchAllReviews')
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
    goToProfile() {
      console.log('클릭', this.review)
      this.$router.push({ name: 'ProfileView', params: {username: this.review.username }})
      const payload = {
        username: this.review.username,
        nickname: this.review.nickname
      }
      this.$store.commit('SAVE_CURR_PROFILE', payload)
    },
    goToReviewDetail() {
      console.log('클릭', this.review)
      this.$router.push({ name: 'ReviewDetailView', params: {review_id: this.review.id }})
    }
  },
  created() {
    this.$emit('fetchAllReviews')
    this.getLikeCount()
  }
}
</script>

<style>
#toggleLike {
  cursor: pointer;
}

</style>