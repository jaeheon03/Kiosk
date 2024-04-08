# 미니 키오스크 만들기

## 페이지 설명
### 1. index 페이지
메뉴이름,평균 평점,가격 같은 간략한 정보를 보여준다.
자세히보기 버튼을 누르면 detail페이지로 넘어간다.
![index](README_images\index.png)
### 2. dtail 페이지
사이즈,온도,옵션을 선택하고 주문하기 버튼을 누르면 order테이블에 저장된다.
![detail](README_images\detail1.png)

밑부분은 리뷰 코멘트와 평점을 볼 수 있는 기능을 추가해보았다.
x버튼을 누르면 리뷰가 삭제된다.
![detail](README_images\detail2.png)

### 3. review_create 페이지
detail 페이지 밑부분 리뷰쓰기 버튼을 누르면 review_create페이지가 나온다.
![review_create](README_images\review_create.png)

### 4. order_list
받은 주문들을 시간 순서대로 볼 수 있다.
x버튼을 누르면 주문이 삭제된다.
![order_list](README_images\order_list.png)


## 모델 설계
메뉴를 중심으로 리뷰,옵션,사이즈,온도,주문 총 5개의 테이블을 만들었다.
![review_create](README_images\models.png)


## 앞으로 구현해보고 싶은점
- 이미지 model을 만들어 시각적으로 보기편하게 만들고싶다
- 여러 model들을 create할 수 있는 하나의 페이지를 만들고 싶다