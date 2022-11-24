<template>
  <div class="mt-3 w-75 mx-auto mb-0">
    <p class="text-light">{{ comment?.content }}&nbsp;
      <span class="delete-comment-btn" style="color: darkred;" @click="deleteComment(review?.id, comment?.id)">X</span>
    </p>
  </div>
</template>

<script>
import api from '@/api/api'
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'MovieCommentItem',
  props: {
    review: Object,
    comment: Object,
  },
  computed: {
    ...mapState([
      'token'
    ])
  },
  methods: {
    deleteComment(reviewId, commentId) {
      axios({
        method: 'delete',
        url: api.movies.deleteReviewComment(reviewId, commentId),
        headers: {
            Authorization: `Token ${this.token}`
          }
        })
        .then((res) => {
          console.log(res)
          alert('정상적으로 삭제되었어요.')
          // 새로고침 안해도 알아서 재렌더링되게 수정해야함..
          // this.$router.go()
          this.$emit('fetchAllReviews')
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style>
.delete-comment-btn {
  cursor: pointer;
}
</style>