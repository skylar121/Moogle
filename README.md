# 🎬 Moogle, 세상의 모든 영화 🎬

![image](https://user-images.githubusercontent.com/100753588/205097355-6f5b5358-66f5-4355-97b8-601f6e24aa8e.png)

## 1️. 프로젝트 개요
- Moogle은 TMDB API를 기반으로 아래와 같은 서비스를 제공합니다 🎥
  1) 영화 정보 검색 및 조회
  2) 영화 추천 (유저 좋아요 기반, 현재 상영중, 장르별)
  3) 영화에 대한 리뷰 작성 및 좋아요 남기기
  4) 유저간 팔로우 기능, 리뷰 댓글 작성 등을 통해 다른 유저들과도 소통할 수 있는 영화 커뮤니티


## 2. 기술 스택
- Front-End
  : HTML, CSS, SCSS, Bootstrap, JavaScript, Vue, Vuex

- Back-End
  : Django, Python, SQLite

## 3. 팀 구성
- 개발 일정 : 11/16 ~ 11/24
- 역할 분담

| **김경림** |   **류태규** |   **정효상**   |
| :--------------: | :------------------: | :-----------------: |
| Vue, JavaScript, <br> Django, Python |   Django, Python |   Vue, JavaScript, <br> Django, Python   |
| ![FrontEnd](https://img.shields.io/badge/FrontEnd-4A06F)![BackEnd](https://img.shields.io/badge/BackEnd-0C4B33)|  ![BackEnd](https://img.shields.io/badge/BackEnd-0C4B33) | ![FrontEnd](https://img.shields.io/badge/FrontEnd-4A06F)![BackEnd](https://img.shields.io/badge/BackEnd-0C4B33) |

<br>



## 4. 프로젝트 구조
- front
```
📦final-pjt-front
┣ 📂public
┗ 📂src
  ┣ 📂api
  ┣ 📂assets
  ┣ 📂components
  ┃ ┣ 📂movie
  ┃ ┗ 📂profile
  ┣ 📂plugins
  ┣ 📂router
  ┣ 📂store
  ┣ 📂views
  ┃ ┣ 📂accounts
  ┃ ┣ 📂movie
  ┣ 📜App.vue
  ┗ 📜main.js
```
- back
```
📦final-pjt-back
 ┣ 📂accounts
 ┣ 📂final_pjt
 ┣ 📂media
 ┃ ┗ 📂users
 ┣ 📂movies
 ┃ ┗ 📂fixtures
 ┣ 📜db.sqlite3
 ┗ 📜manage.py
```

## 5. UI & 주요 기능
| 1. 회원가입 | 2. 로그인 |
|----------|----------|
|<img src="https://user-images.githubusercontent.com/102273370/205475511-37142ee5-ce40-4042-985e-dc3a3cc62923.gif">    | <img src="https://user-images.githubusercontent.com/102273370/205475537-b1429a98-bdc7-400a-bd39-cab80a1b6bc0.gif"> |

| 3. 로그아웃                                                  | 4. 영화추천 (로그인 X)                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://user-images.githubusercontent.com/102273370/205497331-1f4a09c1-85bd-444e-8436-6a60b2fcc7e9.gif"> | <img src="https://user-images.githubusercontent.com/102273370/205497831-151785d9-970e-44a6-9848-b6f193d6fe42.gif"> |

| 3-1. 영화추천 (로그인 O, 좋아요 X) | 3-2. 영화추천 (로그인 O, 좋아요 O) |
|----------|----------|
| <img src="https://user-images.githubusercontent.com/102273370/205498032-5b2b1db7-5462-45cc-a167-6af41d0d6031.gif"> | <img src="https://user-images.githubusercontent.com/102273370/205498154-2e901669-7ad3-4b2d-86fd-70e61c13c0a0.gif"> |

| 4. 현재 상영중, 액션, 로맨스 영화 추천 | 5. 영화 상세 정보 |
|----------|----------|
| <img src="https://user-images.githubusercontent.com/102273370/205498344-98fd85cc-77e7-4563-a820-22b922930288.gif"> | <img src="https://user-images.githubusercontent.com/102273370/205499415-29a6ab0f-16c3-4a29-b0e3-569d64eeaf9c.gif"> |

| 6. 영화 좋아요 (로그인 필요) | 7. 리뷰 작성 |
|----------|----------|
| <img src="https://user-images.githubusercontent.com/102273370/205498452-2d4b40b0-f1db-4cc0-bf20-c9d216508b9f.gif"> | <img src="https://user-images.githubusercontent.com/102273370/205498511-13f7ce24-5be1-45aa-9951-fc6d001b2ab3.gif"> |

| 8. 리뷰 수정, 삭제 | 9. 다른 사람 리뷰 좋아요 및 댓글 |
|----------|----------|
| <img src="https://user-images.githubusercontent.com/102273370/205499463-ffe553b5-38ac-4152-b650-9b4cb4727c9a.gif"> | <img src="https://user-images.githubusercontent.com/102273370/205498601-fd2158e5-746d-4550-8dd0-1b16a0fd0244.gif"> |

| 10. 마이 프로필 |
|----------|
| <img src="https://user-images.githubusercontent.com/102273370/205498897-9a76f1e2-6b06-4de2-b269-1adab7e82845.gif"> |

## 6. 주요 기능 코드
<details>
<summary>선택한 영화가 DB에 있다면 DB 정보 불러오기, 없다면 DB 저장후 해당 정보 불러오기</summary>
<div markdown="1">

```javascript
getMovieDetail() {
  // 먼저 DB에 있는지 확인
  axios({
    method: 'get',
    url: API_URL + `/movies/${this.$route.params.movie_id}/`,
  })
  .then((res) => {
    this.movie = res.data
  })
  .catch((error) => {
    console.log(error)

    // DB에 없으면 TMDB에서 가져온 데이터를 DB에 저장
    axios({
      method: 'get',
      url: API_URL + `/movies/${this.$route.params.movie_id}/`,
      data: {
        id: this.$route.params.movie_id,
      }
    })
      .then((response) => {
        console.log(response)
      })
      .catch((error) => {
        console.log(error)
      })
  })
},
```

</div>
</details>

<br>

<details>
<summary>유저 좋아요 기반 영화 추천</summary>
<div markdown="1">

```python
@api_view(['GET'])
def recommend(request,user_pk):
    print(request)
    file_path = "movies/fixtures/movies.json"

    with open(file_path, 'r', encoding="UTF-8") as f:
        data = json.load(f)
    new_data = []
    for d in data:
        new_data.append({
            'pk': d['pk'],
            'adult': d['fields']['adult'],
            'overview': d['fields']['overview'],
            'title': d['fields']['title'],
            'poster_path': d['fields']['poster_path'],
            'genres': d['fields']['genres'],
            'vote_average': d['fields']['vote_average'],
        })

    new_data = pd.DataFrame(new_data)

    new_data['overview'].isnull().sum()
    new_data['overview'] = new_data['overview'].fillna('')
    new_data['overview'].isnull().sum() #0 으로 바뀜 내적하면 모두 0 나옴

    tfidf=TfidfVectorizer(stop_words='english') #불용어 제거
    tfidf_mat=tfidf.fit_transform(new_data['overview']).toarray()

    def cos_sim2(X,Y):
        return np.dot(X,Y)/((norm(X)*norm(Y))+1e-7)

    def top_match_ar2(new_data, name, rank=5,simf=cos_sim2):
        sim=[]
        for i in range(len(new_data)):
            if name != i:
                sim.append((simf(new_data[i],new_data[name]),i))
        sim.sort()
        sim.reverse()
        return sim[:rank]

    
    user = get_object_or_404(get_user_model(),pk = user_pk)
    lst1 = list(user.like_movies.all().values())    # 좋아요 누른 영화 리스트
    lst = []    # 새로운 리스트
    movieList = []

    if len(lst1) >= 3:                      # 좋아요를 누른 영화가 3개 이상일 경우
        for elt in lst1:
            lst.append(elt['title'])
    else:                                   # 좋아요를 누른 영화가 3개 미만일 경우
        lst1.append(list(Movie.objects.all().values),3 )
        for elt in lst1:
            lst.append(elt['title'])                        
        
    movieList = random.sample(lst,3)
    recommend_lst = set()
    res_list = []
    for movie_name in movieList:
        # 여기에 영화 이름 동적으로 할당
        movie_idx = list(new_data['title']).index(movie_name)
        for sim, movie_id in top_match_ar2(tfidf_mat, movie_idx ,20):
            res_list.append(str({'id': new_data.loc[movie_id,'pk'], 'title' :new_data.loc[movie_id,'title'], 'poster_path' :new_data.loc[movie_id,'poster_path'], 'vote_average' :new_data.loc[movie_id,'vote_average']}))
        for res in res_list[:30]:
            recommend_lst.add(res)
    result = []
    for i in recommend_lst:
        i = eval(i)
        result.append(i)
    return Response(result)
```

</div>
</details>

<br>

<details>
<summary>유저 신규리뷰 작성 & 기존 리뷰 수정, 삭제 로직</summary>
<div markdown="1">

```javascript
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
```

</div>
</details>



## 7. 개발 이슈 및 트러블 슈팅
- 매일 매일 개발 일지를 작성하며 이슈에 대한 트러블 슈팅도 함께 기록하였습니다.
<details>
<summary>트러블슈팅 예시</summary>
<div markdown="1">

![image](https://user-images.githubusercontent.com/100753588/205089044-dc0ff68f-78b0-46ae-8cfb-676223f907e1.png)

</div>
</details>


![image](https://user-images.githubusercontent.com/100753588/205088816-9b5347e8-8f48-4b45-aaf6-35d1bbfd6fcd.png)



## 8. 프로젝트를 마치며
### 김경림
**배운 점**
1. 앱의 모든 기능, 디자인, 컴포넌트 하나하나 직접 담당하여 설계하고 구현해보게 되어 뿌듯했다.
2. 프론트엔드, 백엔드를 함께 기획하고 구현하는 경험은 앞으로도 해보기 쉽지 않을 소중한 경험인 것 같다.
3. 협업시에는 서로 기본 용어에 대해 동일하게 정의하고 생각하고 있는지부터 점검해야 소통이 보다 쉬워진다는 것을 재확인하였다. (알고보면 서로 같은 이야기를 하고 있는 경우가 많다!)
4. SCSS, Vuex 등 추가적으로 도입이 필요한 부분에 대해 고민해보고 당위성을 따져볼 수 있었다.
5. 모듈화의 중요성과 페이지나 컴포넌트 구조를 정확히 생각하고 짜는 것이 중요하다는 것을 배웠다. 예상치 못하게 구조에 변경이 필요할 때 했던 일을 다시 하는 시간과 빈도가 현저하게 줄기 때문이다.

**아쉬운 점**
- 프로젝트 기간이 너무 짧아 git flow, github flow 등 브랜치 전략 및 github의 이슈 등 기본 기능들을 활용하지 못한점이 아쉽다.
- 최적화를 어떻게 더 할수 있을지 알고싶다.
Vuex로 중앙 저장소에서 데이터 관리를 적절하게 한 것인지, 불필요하게 재렌더링이 발생한 부분이 있는지, 있다면 어떻게 더 줄여야 할지 알고 싶다.
- DB 설계시 필드명의 중요성
프론트단에서 해당 데이터의 key로 접근하기 때문에, 이 필드명이 다르면 같은 구조여도 같은 컴포넌트로서 재활용할 수가 없었다.  (프로필 페이지 구현시)
