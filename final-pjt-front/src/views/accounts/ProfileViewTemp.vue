<template>
  <div>
    <header>
      <!-- <img class="background-img" :src="`https://source.unsplash.com/featured/?cinema`"> -->
      <div class="container">
        <div class="profile">
          <div class="profile-image">
            <img :src="this.$route.params.username.profile_image ? 'http://127.0.0.1:8000' + this.$route.params.username.profile_image : null" alt="">
          </div>
          <div class="profile-user-settings">
            <h1 v-if="currUser.username !== nowProfile.username" class="profile-user-name">{{ nowProfile.nickname }}</h1>
            <h1 v-else class="profile-user-name">{{ currUser.nickname }}</h1>
            <!-- <button class="ig-btn profile-edit-ig-btn text-light">Edit Profile</button> -->
            <!-- <button class="ig-btn profile-settings-ig-btn text-light fs-2" aria-label="profile settings"><i class="fas fa-cog" aria-hidden="true"></i></button> -->
            <span v-if="currUser.username !== nowProfile.username">
              <button @click="follow" v-if="isFollowed">언팔로우</button>
              <button @click="follow" v-if="!isFollowed">팔로우</button>
            </span>
            <!-- <span v-else>
              프로필 수정
            </span> -->
          </div>
          <div class="profile-stats">
            <ul>
              <li><span class="profile-stat-count">{{ followers }}</span> followers</li>
              <li><span class="profile-stat-count">{{ followings }}</span> following</li>
            </ul>
          </div>
          <div class="profile-stats">
            <ul>
              <li><span class="profile-stat-count">164</span> watched</li>
              <li><span class="profile-stat-count">188</span> liked</li>
            </ul>
          </div>
          <!-- <div class="profile-bio">
            <p><span class="profile-real-name">Jane Doe</span> Loem ipsum dolor sit, amet consectetur adipisicing elit 📷✈️🏕️</p>
          </div> -->


        </div>
        <!-- End of profile section -->
      </div>
      <!-- End of container -->
      </header>
      <main>
      <div class="container">
        <div class="gallery">
          <ProfileListItem v-for="review in userReviews" :key="review.id" :review="review" @click="goToDetail(review.movie)"  />
        </div>
        <!-- End of gallery -->
        <!-- <div class="loader"></div> -->
      </div>
      <!-- End of container -->
      </main>
  </div>

</template>

<script>
import axios from 'axios'
import api from "@/api/api"
import { mapState, mapActions } from 'vuex'
import ProfileListItem from '@/components/profile/ProfileListItem'

export default {
  name: 'ProfileView',
  components: {
    ProfileListItem,
  },
  data() {
    return {
      followers: 0,
      followings: 0,
      isFollowed: false,
    }
  },
  computed: {
    ...mapState([
      'token',
      'currUser',
      'currProfile',
    ])
  },
  methods: {
    ...mapActions([
      'getUserReviews',
    ]),
    goToDetail(id) {
      console.log('클릭', id)
      this.$router.push({ name: 'DetailView', params: { movie_id: id }})
    },
    follow() {
      console.log(this.token)
      axios({
        method: 'post',
        url: api.accounts.follow(this.$route.params.username),
        headers: {
          Authorization: `Token ${this.token}`
        }
      })
      .then((res) => {
        console.log('팔로잉워', res)
        this.isFollowed = res.data.is_follow
        this.followers = res.data.followers
        this.followings = res.data.followings
        // this.isFollowed = res.data.length
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getInitialFollowers() {
      console.log(this.$route.params.username)
      console.log(api.accounts.followers(this.$route.params.username))
      axios({
        method: 'get',
        url: api.accounts.followers(this.$route.params.username)
      })
      .then((res) => {
        this.followers = res.data.length
        console.log('팔로워수', res.data.length)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getInitialFollowings() {
      console.log(api.accounts.followers(this.$route.params.username))
      axios({
        method: 'get',
        url: api.accounts.followings(this.$route.params.username)
      })
      .then((res) => {
        this.followings = res.data.length
        console.log('팔로잉수', res.data.length)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  created() {
    this.getUserReviews()
    this.getInitialFollowers()
    this.getInitialFollowings()
  }
}
</script>

<style lang="scss">
.profile {
  /* border: 1px solid $primary; */
  background-color: rgb(44, 44, 44);
}

.profile-stats > ul {
  border: none;
}

/*

All grid code is placed in a 'supports' rule (feature query) at the bottom of the CSS (Line 310). 
        
The 'supports' rule will only run if your browser supports CSS grid.

Flexbox and floats are used as a fallback so that browsers which don't support grid will still recieve a similar layout.

*/

/* Base Styles */

/* body {
    font-family: "Open Sans", Arial, sans-serif;
    min-height: 100vh;
    background-color: #fafafa;
    color: #262626;
    padding-bottom: 3em;
}

img {
    display: block;
}

.container {
    max-width: 93.5em;
    margin: 0 auto;
    padding: 0 2em;
} */

.ig-btn {
    display: inline-block;
    font: inherit;
    background: none;
    border: none;
    color: inherit;
    padding: 0;
    cursor: pointer;
}

.ig-btn:focus {
    outline: 0.5em auto #4d90fe;
}

.visually-hidden {
    position: absolute !important;
    height: 1px;
    width: 1px;
    overflow: hidden;
    clip: rect(1px, 1px, 1px, 1px);
}

/* Profile Section */

.profile {
    padding: 5em 0;
}

.profile::after {
    content: "";
    display: block;
    clear: both;
}

.profile-image {
    float: left;
    /* width: calc(33.333% - 1em); */
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 3em;
}

.profile-image img {
    border-radius: 50%;
}

.profile-user-settings,
.profile-stats,
.profile-bio {
    float: left;
    /* width: calc(66.666% - 2em); */
}

.profile-user-settings {
    margin-top: 1.1em;
}

.profile-user-name {
    display: inline-block;
    font-size: 3.2em;
    font-weight: 300;
}

.profile-edit-ig-btn {
    font-size: 1.4em;
    line-height: 1.8;
    border: 0.1em solid #dbdbdb;
    border-radius: 0.3em;
    padding: 0 2.4em;
    margin-left: 2em;
}

.profile-settings-ig-btn {
    font-size: 2em;
    margin-left: 1em;
}

.profile-stats {
    margin-top: 2.3em;
}

.profile-stats li {
    display: inline-block;
    font-size: 1.6em;
    line-height: 1.5;
    margin-right: 4em;
    cursor: pointer;
}

.profile-stats li:last-of-type {
    margin-right: 0;
}

.profile-bio {
    font-size: 1.6em;
    font-weight: 400;
    line-height: 1.5;
    margin-top: 2.3em;
}

.profile-real-name,
.profile-stat-count,
.profile-edit-ig-btn {
    font-weight: 600;
}

/* Gallery Section */

.gallery {
    display: flex;
    flex-wrap: wrap;
    margin: -1em -1em;
    padding-bottom: 3em;
}

.gallery-item {
    position: relative;
    flex: 1 0 22em;
    margin: 1em;
    color: #fff;
    cursor: pointer;
}

.gallery-item:hover .gallery-item-info,
.gallery-item:focus .gallery-item-info {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.3);
}

.gallery-item-info {
    display: none;
}

.gallery-item-info li {
    display: inline-block;
    font-size: 1.7em;
    font-weight: 600;
}

.gallery-item-likes {
    /* margin-right: 2.2em; */
}

.gallery-item-type {
    position: absolute;
    top: 1em;
    right: 1em;
    font-size: 2.5em;
    text-shadow: 0.2em 0.2em 0.2em rgba(0, 0, 0, 0.1);
}

.fa-clone,
.fa-comment {
    transform: rotateY(180deg);
}

.gallery-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Loader */

.loader {
    width: 5em;
    height: 5em;
    border: 0.6em solid #999;
    border-bottom-color: transparent;
    border-radius: 50%;
    margin: 0 auto;
    animation: loader 500ms linear infinite;
}

/* Media Query */

@media screen and (max-width: 40em) {
    .profile {
        display: flex;
        flex-wrap: wrap;
        padding: 4em 0;
    }

    .profile::after {
        display: none;
    }

    .profile-image,
    .profile-user-settings,
    .profile-bio,
    .profile-stats {
        float: none;
        width: auto;
    }

    .profile-image img {
        width: 7.7em;
    }

    .profile-user-settings {
        /* flex-basis: calc(100% - 10.7em); */
        display: flex;
        flex-wrap: wrap;
        margin-top: 1em;
    }

    .profile-user-name {
        font-size: 2.2em;
    }

    .profile-edit-ig-btn {
        order: 1;
        padding: 0;
        text-align: center;
        margin-top: 1em;
    }

    .profile-edit-ig-btn {
        margin-left: 0;
    }

    .profile-bio {
        font-size: 1.4em;
        margin-top: 1.5em;
    }

    .profile-edit-ig-btn,
    .profile-bio,
    .profile-stats {
        flex-basis: 100%;
    }

    .profile-stats {
        order: 1;
        margin-top: 1.5em;
    }

    .profile-stats ul {
        display: flex;
        text-align: center;
        padding: 1.2em 0;
        /* border-top: 0.1em solid #dadada;
        border-bottom: 0.1em solid #dadada; */
    }

    .profile-stats li {
        font-size: 1.4em;
        flex: 1;
        margin: 0;
    }

    .profile-stat-count {
        display: block;
    }
}

/* Spinner Animation */

@keyframes loader {
    to {
        transform: rotate(360deg);
    }
}

/*

The following code will only run if your browser supports CSS grid.

emove or comment-out the code block below to see how the browser will fall-back to flexbox & floated styling. 

*/

@supports (display: grid) {
    .profile {
        display: grid;
        grid-template-columns: 1fr 2fr;
        grid-template-rows: repeat(3, auto);
        grid-column-gap: 3em;
        align-items: center;
    }

    .profile-image {
        grid-row: 1 / -1;
    }

    .gallery {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(22em, 1fr));
        grid-gap: 2em;
    }

    .profile-image,
    .profile-user-settings,
    .profile-stats,
    .profile-bio,
    .gallery-item,
    .gallery {
        width: auto;
        margin: 0;
    }

    @media (max-width: 40em) {
        .profile {
            grid-template-columns: auto 1fr;
            grid-row-gap: 1.5em;
        }

        .profile-image {
            grid-row: 1 / 2;
        }

        .profile-user-settings {
            display: grid;
            grid-template-columns: auto 1fr;
            grid-gap: 1em;
        }

        .profile-edit-ig-btn,
        .profile-stats,
        .profile-bio {
            grid-column: 1 / -1;
        }

        .profile-user-settings,
        .profile-edit-ig-btn,
        .profile-settings-ig-btn,
        .profile-bio,
        .profile-stats {
            margin: 0;
        }
    }
}

</style>