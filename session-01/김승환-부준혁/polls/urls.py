from django.urls import path

from . import views

app_name = "polls"
#app이 많아지면 템플릿에서 url 'detail'처럼 사용하였을 때
# 이 앱들의 url을 구별하기 위해 
#app_name을 추가하여 앱의 이름 공간을 설정해준다.
# 이제 템플릿에서 url 'polls:detail' 처럼 상세 뷰를 가리킬 수 있도록 코드를 작성하면 장고가 뷰를 쉽게 구분 할 수 있다.
# urlpatterns = [

#     # ex: /polls/
#     path("", views.index, name="index"),
#     #전달 받은 값이 아무것도 없으면 view.index로 연결을 시켜준다.

#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     #question_id를 인수로 전달하면, views.함수에서 값을 받아서 사용한다.

#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]  

# 코드를 적게 사용하기 위한 제네릭 뷰에
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # name 매개변수는 해당 URL 패턴에 대한 고유한 이름을 지정하는 것으로, 
    # 이를 이용해 템플릿 등에서 URL 패턴을 참조할 수 있다.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
] #
    #URL에서 값을 캡처하기 위해 꺾쇠 괄호를 사용한 것.
    #모든 URL에 슬래시가 있으므로 선행 슬래시는 사용하지 않는다.

# path(route,view,kwargs(선택),name(선택))함수의 인수
# route : url 패턴을 가진 문자열로 urlpatterns 의 첫 번째 패턴부터 시작하여, 일치하는 패턴을 찾을 때 까지 요청된 URL 을 각 패턴과 리스트의 순서대로 비교합니다.
# 패턴들은 GET 이나 POST 의 매개 변수들, 혹은 도메인 이름을 검색하지 않습니다. 예를 들어, https://www.example.com/myapp/ 이 요청된 경우, URLconf 는 오직 myapp/ 부분만 바라 봅니다. https://www.example.com/myapp/?page=3, 같은 요청에도, URLconf 는 역시 myapp/ 부분만 신경씁니다.

# view : 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고, 경로로 부터 ‘캡처된’ 값을 키워드 인수로하여 특정한 view 함수를 호출합니다. 나중에 이에 대한 간단한 예제를 살펴보겠습니다.

# name : URL 에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있습니다. 이 강력한 기능을 이용하여, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있도록 도와줍니다.
