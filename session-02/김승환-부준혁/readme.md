최적화를 위해서 해야할 것
같은 기능을 하는 것은 어느정도 묶기 
시간이 나면 class형 view를 사용하기
url을 분할하기
html을 include를 사용해서 통일하기

post와 get을 구분하는 이유 
같은 url로 함수를 실행시키더라도 post일 때는 값을 받아서 create, update, delete를 할 수 있고
get일 때는 단지 read만 하거나 post를 할 html만을 불러오게 할 수 있다.
(처음에는 이를 잘 몰라서 한 url당 post를 작성할 html로 이동하는 함수, post로 받은 값을 처리하는 함수 두 개를 짤 뻔했다.)