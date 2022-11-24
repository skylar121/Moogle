<template>
  <div class="container d-flex align-items-center">
    <div class="col py-5">
      <div class="row justify-content-center">
        <div class="col-md-10 col-lg-8">
          <!-- Back Button -->
          <div class="mb-4">
            <router-link :to="{ name: 'reviewList' }">
              <button class="btn btn-outline-light btn-sm">
                <i class="fa-solid fa-chevron-left"></i>&nbsp;&nbsp;글 목록
              </button>
            </router-link>
          </div>
          <!-- review -->
          <div>
            <div class="review-title my-4">
              <h2>{{ review.title }}</h2>
            </div>
            <div class="review-info mb-5 d-flex justify-content-between">
              <div>
                <router-link :to="{ name: 'profile', params: { username: review.user.username }}">
                  {{ review.user.username }}
                </router-link>&nbsp;|&nbsp;
                {{ review.created_at | date }} 작성&nbsp;|&nbsp;
                {{ review.updated_at | date }} 수정&nbsp;|&nbsp;
                <i class="fa-regular fa-thumbs-up"></i> {{ review.like_count }}&nbsp;
                <i class="fa-regular fa-message"></i> {{ review.comment_set.length }}
              </div>
              <div>
                <router-link v-if="isAuthor" :to="{ name: 'reviewEdit', params: { reviewPk }}">
                  <i class="fa-regular fa-pen-to-square"></i> 수정
                </router-link>&nbsp;
                <a v-if="isAuthor" class="delete-btn">
                  <button @click="deletereview(reviewPk)">
                    <i class="fa-regular fa-trash-can"></i> 삭제 
                  </button>
                </a>
              </div>
            </div>
            <div class="review-content">
              <p>{{ review.content }}</p>
            </div>
          </div>

          <!-- review Like -->
          <div class="review-like">
            <button v-if="review.like_users.find((user) => user.pk === currentUser.pk)" class="like-btn" @click="likereview(reviewPk)">
              <!-- <i class="fa-solid fa-heart"></i>  -->
              <i class="fa-solid fa-thumbs-up"></i> <span>좋아요 취소</span>
            </button>
            <button v-else class="like-btn" @click="likereview(reviewPk)">
              <!-- <i class="fa-regular fa-heart"></i>  -->
              <i class="fa-regular fa-thumbs-up"></i> <span>좋아요</span>
            </button>
          </div>
          <hr />
          <!-- Comments -->
          <comment-list :comments="review.comment_set"></comment-list>
        </div>
      </div>
    </div>




  </div>
</template>

<script>

export default {
    name: 'ReviewDetailView',
    components: {
    },
    data() {
      return {
        // reviewPk: this.$route.params.reviewPk
      }
    },
    // computed: {
    //   ...mapGetters(['review', 'isAuthor', 'currentUser']),
    //   likeCount() {
    //     return this.review.like_users?.length
    //   }
    // },
    // methods: {
    //   ...mapActions(['fetchreview', 'deletereview', 'likereview']),
    // },
    // filters: {
    //   date(dateField) {
    //     return moment(String(dateField)).format('YYYY/MM/DD HH:mm')
    //   }
    // },
    // created() {
    //   this.fetchreview(this.reviewPk)
    // }
}
</script>

<style>
.review-title {

}

.review-info {
  color: #cdcdcd;
  font-size: 0.9rem;
}

.delete-btn button {
  color: #ffffff;
  background: none;
  border: none;
}

.delete-btn button:hover {
  color: #90b8f8;
  text-decoration: underline;
}

.review-content {
  white-space: pre-wrap;
}

.review-like button {
  color: #ffffff;
  background: none;
  border: none;
}
</style>