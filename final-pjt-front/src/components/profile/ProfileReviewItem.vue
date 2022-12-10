<template>
  <div @click="goToDetail" class="gallery-item" tabindex="0">
    <img :src="review?.movie_backdrop_path ? 'https://image.tmdb.org/t/p/original' + review?.movie_backdrop_path : 'https://image.tmdb.org/t/p/original' + review?.movie_poster_path" class="gallery-image" alt="">
    <div class="gallery-item-info">
      <ul>
        <div class="mx-auto my-0 text-center">
          <li class="gallery-item-likes">{{ review?.movie_title }}</li>
          <p class="fs-5">"{{ review?.title }}"</p>
          <div class="mx-auto my-0 text-center">
            <li class="gallery-item-likes fs-5">좋아요 <i class="fas fa-heart" aria-hidden="true"></i><span class="me-4"> {{ likeCount }}</span></li>
            <li class="gallery-item-comments fs-5">댓글 <i class="fas fa-comment" aria-hidden="true"></i> {{ reviewCount }}</li>
          </div>
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import api from '@/api/api'
import { mapState } from 'vuex'

export default {
  name: 'ProfileReviewListItem',
  props: {
    review: Object,
  },
  data() {
    return {
      reviewComments: null,
    }
  },
  computed: {
    ...mapState([
      'token',
    ]),
    likeCount() {
      return this.review?.like?.length
    },
    reviewCount() {
      return this.reviewComments?.length
    }
  },
  methods: {
    goToDetail() {
      // console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: this.review?.movie }})
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
          this.reviewComments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getReviewComments()
  }
}
</script>

<style>

</style>