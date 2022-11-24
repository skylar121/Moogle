<template>
  <div class="card review-card col w-75 text-center mx-auto my-0">
    <!-- <div @click="goToReviewDetail" class="card review-card"> -->
    <div class="text-bg-dark card-header d-flex justify-content-between align-items-center">
      <div class="text-light">
        <!-- <img :src="review?.user" alt=""> -->
        <strong>{{ review.nickname }}</strong>
      </div>
      <div class="text-light">
        <button v-if="currUser.username !== review.username"  @click="goToProfile" class="btn btn-primary">프로필 보기</button>
        <button v-if="currUser.username === review.username" @click="deleteReview" class="btn btn-primary"><i class="fa-solid fa-trash-can" style="cursor: pointer"></i></button>
      </div>
    </div>

    <div
      class="card-body d-flex flex-column justify-content-center align-items-center">
      <p class="card-title text-light fs-3">{{ review.title }}</p>
      <p class="card-text text-muted">{{ review.content }}</p>
      <!-- <p v-if="review.content.length > 50" class="card-text text-muted">{{ `${review.content.slice(0,50)} ...더보기` }}</p>
      <p v-else class="card-text text-muted">{{review.content}}</p> -->
      <div class="movieVoteAverage">
        <b-form-rating
          :value="review.rank"
          readonly
          show-value
          precision="1"
          color="#ffd21e"
          class="border-0 text-light"
          size="lg"
        ></b-form-rating>
        <!-- <p>{{ movie?.vote_average.toFixed(1) > 0.0 ? `⭐${movie?.vote_average.toFixed(1)} / 10` : '아직 별점이 없어요!' }} </p> -->
      </div>
      <!-- <a href="#" class="btn btn-primary">Go somewhere</a> -->
    </div>

    <div class="card-footer text-muted d-flex justify-content-between">
      <div class="fs-5">
        <span v-if="!initialHeart">
          <i class="fa-regular fa-heart me-2"  style="color: #dd3c3c;" id="toggleLike" @click="toggleLike"></i>
        </span>
        <span v-else>
          <i class="fa-solid fa-heart me-1"  style="color: #dd3c3c;" id="toggleLike" @click="toggleLike"></i>
        </span>
        <span class="me-2" style="color: #dd3c3c;">{{ likeCount }}</span>
        <i class="fa-regular fa-comment mx-1" style="cursor: pointer"></i>
        <span class="me-2">{{ commentCount }}</span>
        <button @click="goToReviewDetail()">자세히 보기</button>
        <div class="accordion" id="accordionExample">
          <MovieCommentItem v-for="comment in comments" :comment="comment" :key="comment.id" />
        </div>
      </div>
      {{ review.updated_at.slice(0, 10) }}
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import api from '@/api/api'
import MovieCommentItem from '@/components/movie/MovieCommentItem'

import { mapState } from 'vuex'
export default {
  name: 'MovieReviewItem',
  components: {
    MovieCommentItem
  },
  props: {
    review: Object,
  },
  data() {
    return {
      likeCount: null,
      initialHeart: false,
      comments: null,
    }
  },
  computed: {
    ...mapState([
      'token',
      'currUser'
    ]),
    commentCount() {
      return this.comments?.length
    }
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
      this.$router.push({ name: 'ReviewDetailView', params: {review_id: this.review.id}})
    },
    getReviewComments() {
      axios({
        method: 'get',
        url: api.movies.getReviewComments(this.review.id),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          this.comments = res.data
          console.log(this.comments)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.$emit('fetchAllReviews')
    this.getLikeCount()
    this.getReviewComments()
    console.log('리뷰정보' , this.review)
  }
}
</script>

<style>
#toggleLike {
  cursor: pointer;
}

</style>