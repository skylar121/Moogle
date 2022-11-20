<template>
  <div class="profile">
    <!-- <img class="background-img" :src="`https://source.unsplash.com/featured/?cinema`"> -->
    <div class="card text-center">
      <div class="card-header">
        <ul class="nav nav-tabs card-header-tabs">
          <li class="nav-item">
            <a class="nav-link active" aria-current="true" href="#">Active</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
        </ul>
      </div>
      <div class="card-body">
        <h5 class="card-title">Profile</h5>
        <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        <a href="#" class="btn btn-primary">평가 더 남기러가기</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
}
</script>

<style>
.profile {
  border: 1px solid pink;
}
</style>