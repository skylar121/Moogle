<template>
  <div class="card review-card ">
    <div class="card-header text-bg-primary">
      {{ review.userName }}
    </div>
    <div class="card-body d-flex flex-column justify-content-center align-items-center">
      <p class="card-title fs-3">{{ review.title }}</p>
      <p class="card-text text-muted">{{ review.content }}</p>
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
          <i class="fa-solid fa-heart" id="toggleLike" @click="toggleLike"></i>
        </span>
        <span>{{ likeCount }}</span>
        <i class="fa-regular fa-comment me-2"></i>
        <i v-if="currUser.username === review.username" @click="deleteReview" class="fa-solid fa-trash-can"></i>
      </div>
      {{ review.updated_at.slice(0, 10) }}
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import api from '@/api/api'

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
          console.log('댓글정보')
          console.log(res.data)
          this.likeCount = res.data.like.length()
          if (res.data.like.has(this.currUser.id)) {
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