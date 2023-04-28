# 이곳에 발표자료를 구성해주세요!

- 추가적인 파일 구성은 자유롭게 해주세요.
가상환경
프로젝트를 여러 개 개발할 때는 패키지의 버전 문제가 발생합니다.  -> 이런 문제 해결 위해 파이썬에서는 가상환경 제공
가상 환경은 독립된 공간을 만들어주는 기능입니다. 
파이썬 실행 파일(인터프리터) 자체도 포함되므로 각 가상 환경 별로 다른 버전의 파이썬 이 들어갈 수 있습니다. 
따라서 스크립트를 실행할 때는 원래 설치된 파이썬이 아닌 가상 환경 안의 파이썬을 사용합니다.

가상환경 세팅 virtualenv 사용
pip install virtualenv
virtualenv 가상환경이름
path\to\가상환경이름\Scripts\activate <- 가상환경실행
그 후 이곳에 장고를 설치
pip install django

프로젝트 만들기
cd 명령으로 프로젝트를 저장할 디렉토리 이동후 아래 명령수행
django-admin startproject mysite(프로젝트 이름)

!!mmsite/settings.py: 현재 Django 프로젝트의 환경 및 구성을 저장하는 파일이다.

!!mmsite/urls.py : Django project 의 URL 선언(매핑)을 저장한다. url로 접속 시, 입력한 url에 따라 어떤 view에 매핑할지 작성해둔 코드이다.
-로그설정
  기본은 True로 되어있어 개발시 로그을 남기게 된다.
-APP 등록
 생성한 APP의 파일들을 모두 등록해준다.
-Templates 설정
 공통적으로 들어가는 html코드를 관리하기 위한 확장형 template들의 경로를 설정할 수 있다.
그외 DB설정, 다국어 및 지역 시간 설정,정적파일 설정(CSS, JavaScript, Images와 같은 정적 파일 경로를 설정) 등이 있다.

장고 동작원리
클라이언트로 부터 요청(Request)를 받으면 URLconf 모듈을 이용하여 URL을 분석한다.
URL 분석 결과를 통해 해당 URL에 매칭되는 View를 실행한다.
View는 자신의 로직을 실행하고, 데이터베이스 처리가 필요하면 Model을 통해 처리하고 그결과를 반환 받는다.
View는 자신의 로직 처리가 끝나면 Template을 사용하여 클라이언트에 전송할 HTML 파일을 생성한다.
View는 최종 결과로 HTML 파일을 클라이언트에게 보내 응답(Response)한다.

개발서버 실행
python manage.py runserver

마이그레이션(migration)이란?
:테이블 및 필드의 생성, 삭제, 변경 등과 같이 데이터베이스에 대한 변경사항을 알려주는 것이라고 합니다.
클래스 모델을 만들고 makemigrations 명령어를 입력해서
DB쪽에서 테이블을 생성할 수 있도록  migrate 한다

python manage.py makemigrations
python manage.py migrate

모델 만들기 (모델은 부가적인 메타데이터를 가진 DB layout)

데이터가 어떻게 전달?
사용자가 submit 타일의 input태그를 누르면 해당 url로
데이터가 전달되고 해당 url에 걸려있는 view에서 데이터를 처리 한 후 어떠한 html로 데이터를 보낸다.

{% csrf_token %} 사이트가 위조요청(사용자와 서버 사이의 데이터를 해커가 임의로 변경하는 행위) 방지위해

view는 여러 함수들을 생성하며, 이 함수들을 통해 데이터를 처리한 뒤, 어떤 html로 데이터를 보낸다.

HttpResponse :html 파일을 따로 사용하지 않고, 클라이언트에게 response(요청에 대한 반응)을 던져줄 수 있다.

render(): request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으며 context 사전형 객체를 선택적 인수로 세번째에 받음
(템플릿에 context를 채워 표현한 결과를 HttpResponse로 감싸서 반환)
return render(request, 'polls/index.html', context)

path(): urlpatterns의 포함되는 요소들을 반환.

템플릿: 템플릿은 HTML 파일과 비슷하지만 파이썬 데이터를 읽어서 사용할수 있는 Dynamic 한 HTML 파일이다.

템플릿 시스템은 변수의 속성에 접근하기 위해 dot-lookup 문법 사용
{{}}는 변수를 의미하고 context로부터 온 value 값을 나타냄

HTTP 응답상태 코드
!! 200: 요청이 정상적으로 처리됨
!! 404: 지정된 URL을 처리하기 위한 자원이 존재하지 않음(파일이 없음)
그외..
400: 클라이언트의 요청이 잘못된 구문으로 구성됨
405: 요청된 메소드가 허용되지 않음
500: 서버 내부 오류
503: 서버가 일시적으로 서비스를 제공할 수 없음

템플릿에서 하드코딩된 URL 제거하기
polls/index.html에 url이 하드코딩되어있음
=> 수많은 템플릿을 가진 프로젝트들의 URL 바꾸는게 어려워짐

<li><a href="/polls/{{question.id}}/">{{question.question_text}}</a></li>
urlpatterns를 정의할 때 path()함수에서 name을 다 설정해줬음

<li><a href="{%url 'detail' question.id%}">{{question.question_text}}</li>
템플릿의 {%url%} 태그를 사용해 하드코딩 URL 제거 및 URL 경로들의 의존성 제거 가능

실제 장고 프로젝트는 앱이 여러개 올 수 있음
=> 여러 앱들의 URL을 어떻게 구별할까요?
1. URLconf에 namespace 추가
polls/urls.py 파일에 app_name을 추가해서 앱의 이름공간 설정할 수 있음

2. polls/index.html에서 이름공간으로 나누어진 상세 뷰를 가리키도록 변경
<li><a href="{%url 'polls:detail' question.id%}">{{question.question_text}}</a></li>

pk: DB내의 하나의 열(데이터)을 구분할 수 있는 값, 중복되지않음

get은 데이터 조회를 위한 요청 방식 하나의 뷰 함수 내의 Get or post 둘다 접근 가능..?

테스트코드: 작성한 코드들에 대해서 제대로 작성했는지 확인하는 코드.

이유1: 앞으로 우리들이 작성할 코드는 끊임없이 수정,개발 을 한다 -> 버그가 나올것 
이유2: 많은 사람들과의 협업을 하기 때문에..