## cmd 명령어에 대해서
##### pip install virtualenv
virtualenv myenv 명령어를 작성 시 "virtualenv는 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는 배치 파일이 아닙니다" 라는 에러 발생 
따라서 제가 가상환경을 저장하고 싶은 공간에 새롭게 폴더를 만들고 터미널에서 그 디렉토리로 이동하여 
##### python -m venv “myenv” 
이런 식으로 가상환경을 세팅하는 방법을 택하였습니다. 

#### virtualenv와 venv의 차이
virtualenv는 Python 2와 Python 3.2 이하를 지원하고, 시스템 패키지를 사용하거나 activate 스크립트를 자동으로 생성하는 기능이 있습니다.    
반면, python -m venv는 Python 3.3 이상을 지원하고 Python에 내장되어 있으며 activate 스크립트를 생성하지 않습니다.

#### 가상환경 실행과 사이트 구축
가상환경을 실행하고 싶다면 가상환경 안의 Scripts 폴더에 들어가서 activate.bat이라는 파일을 실행시켜준다.

가상환경을 만드는 이유 -> 가상환경 마다 다른 개발환경을 구축할 수 있기 때문
프로젝트 시작 시 django-admin startproject mysite를 사용하여 사이트 구축

##### py manage.py runserver
서버를 구동시키기 위해 이용하는 명령어
미적용 마이그레이션에 관한 경고 메시지가 생성되었습니다.
장고 프로젝트의 루트 디렉토리에서 python manage.py migrate를 통해 미적용 마이그레이션 경고를 해결하였습니다.

>#### migration이란?
>데이터베이스의 구조를 관리하는 명령어로서 우리가 Django 프로젝트를 개발하다가, 모델을 수정하거나 새로운 모델을 추가하면, 데이터베이스에도 그것을 반영해줘야 합니다. 그래야만 모델의 변경사항을 데이터베이스에서도 사용할 수 있기 때문입니다. 즉, migrate 명령어는 Django에서 모델과 데이터베이스 간의 일관성을 유지하고, 모델의 변경사항을 데이터베이스에 적용하는 역할을 합니다.
>makemigrations는 마이그레이션 파일을 생성하고, migrate는 마이그레이션 파일을 실행하여 실제 데이터베이스 스키마를 변경합니다.

##### py manage.py startapp polls
Python 어플을 만드는 명령어 장고 프로젝트의 루트 디렉토리에서 polls라는 이름의 어플을 생성해줍니다.

##### py manage.py createsuperuser
관리자 사이트를 생성하는 명령

<hr>

## 장고에 대해서
![request_cycle](https://user-images.githubusercontent.com/69035864/235091437-e835dea4-5596-4e9e-9b39-c7f9adceeec1.jpg)
 장고를 이해하기 위해서는 장고의 request cycle에 대한 이해가 선행되어야 한다고 생각합니다.

   1. client가 웹에 대한 정보를 요청
   2. Nginx/Apache와 같은 web server가 요청을 받음 (장고에서는 개발을 위한 경량 개발 웹서버가 제공된다. 하지만 배포할 때는 Nginx/Apache와 같은 web server를 이용하여 배포해야 한다.)
   3. wsgi를 통해 웹서버와 장고 프레임워크를 연결해준다. 
   4. 사용자가 특정 주소를 요청한다.
   5. url 파일에서 요청한 주소를 잘게 나눈다.(파싱)
   6. 잘게 나눠진 주소는 view.py로 이동한다. (view에는 웹사이트를 위한 코드들이 있다.) ex) 데이터 저장, 데이터 베이스에서 꺼내옴
   7. Template에서 디자인 담당 (html)
   8. Template가 response를 받는다.

### django-admin startproject시 생성되는 파이썬 파일들.
* __init__.py: 이 디렉토리를 Python 패키지로 간주해야 함을 Python에 알리는 빈 파일입니다.
* settings.py: 이 Django 프로젝트에 대한 설정/구성입니다.
* urls.py: 이 Django 프로젝트에 대한 URL 선언
* wsgi.py: 웹서버와 장고 프레임워크를 연결해준다.

### py manage.py startapp을 하게 되면 생성되는 파이썬 파일들
* admin.py : 관리자 사이트에서 모델을 어떻게 보여줄지, 어떤 액션을 취할지 등을 정의합니다.
* apps.py : 프로젝트의 앱들에 대한 설정을 담고 있습니다. 앱 이름, 별칭, 설정 등을 관리합니다.
* models.py : 데이터베이스의 테이블을 정의하는 역할을 합니다. 이 파일에서는 각 테이블의 필드와 관계를 정의할 수 있습니다.
>### DRY 원칙이란?
>models.py에서는 Question과 Choice라는 두 개의 클래스를 만들어 활용하였습니다. Question과 Choice를 만들어놓고 적재적소에 활용하기 위함입니다. 이렇게 만들지 않았다면, 아마 중복된 코드를 여기저기에 만들고 사용해야 했을 것입니다. 이와 관련한 원칙을 DRY 원칙이라고 합니다.
>#### Don't Repeat Yourself
>중복 코드를 최소화하고 유지보수성, 확장성, 재사용성 등을 개선하기 위한 설계 원칙입니다. 이 원칙은 코드의 중복을 피하고, 코드를 수정할 때에는 최소한의 수정으로 원하는 결과를 얻을 수 있도록 설계해야 한다는 의미입니다.
>DRY 원칙을 준수하는 코드는 다음과 같은 특징을 가집니다.
>* 코드의 중복이 최소화된다.
>* 코드의 유지보수성이 높아진다.
>* 코드의 재사용성이 높아진다.
>* 코드의 확장성이 높아진다.
>
> DRY 원칙은 코드의 재사용성을 높이기 위해 함수, 클래스, 모듈 등을 잘게 나누는 것을 권장합니다. 또한 코드의 중복을 최소화하기 위해 상수, 변수, 함수 등을 재사용하고, 코드를 수정할 때에는 최소한의 수정으로 원하는 결과를 얻을 수 있도록 설계해야 한다는 의미입니다. 
* tests.py : 각 모델, 뷰, 폼, 템플릿 등의 유효성 검사를 작성할 수 있습니다.
* urls.py : URL 패턴을 정의합니다. 웹 브라우저로부터 요청이 오면, 해당 요청을 처리하는 뷰를 찾아내기 위해 URL 패턴을 검색합니다.
> #### URLConf란?
>urls.py 파일에서 코드를 작성하다 보면 URLConf라는 단어가 많이 나옵니다. URLConf는 뭘까요?
>URLConf는 URL Configuration의 약어로 URL과 view를 매핑(연결)하는 설정입니다. 
>URLConf를 이용하여 Django 앱의 URL을 정의하고, 각 URL을 해당하는 뷰(View)나 다른 URLConf와 연결합니다.
* views.py : 애플리케이션의 비즈니스 로직을 작성합니다. 이 파일에서는 요청을 처리하고, 데이터를 처리하고, 응답을 생성하는 함수를 작성할 수 있습니다.
* manage.py : Django 프로젝트의 유틸리티 스크립트입니다. 서버를 시작하거나 데이터베이스를 관리하는 등의 작업을 수행할 수 있습니다.

#### Django Template 언어
장고에서 HTML 파일을 작성할 때 사용하는 문법으로 HTML과 유사하지만, Django에서 제공하는 특별한 문법을 사용할 수 있습니다.
##### {{ }} 중괄호
Python 코드에서 생성한 값을 출력하기 위해 사용하며 변수를 중괄호 안에 둘러싸서 활용합니다.
예를 들어, {{ my_variable }}은 my_variable이라는 변수의 값을 출력합니다
##### {{% %}} 중괄호와 퍼센트기호
if문, for문 등의 제어문을 사용하기 위해 사용합니다,
예를 들어, if문은 {% if %}로 시작하여 {% endif %}로 끝내고,
for in 문은  {% for i in object %}로 시작하여 {% endfor %} 로 끝냅니다.
   
추가적으로 주석은 {# 주석 #} 이런 방식으로 생성할 수 있습니다.
## 느슨한 결합
장고 도큐먼트에 따르면 , Django 스택의 근본적인 목표는 느슨한 결합, 탄탄한 응집이라고 나와있습니다. 프레임워크의 각 계층은 정말로 필요하기 전에는 서로 “알지 못해야” 한다는 의미입니다.

예를 들어, 템플릿 시스템은 웹 요청에 대해 아무 것도 모르고, DB 계층은 데이터 표시에 대해 아무 것도 모르고, View 시스템은 프로그래머가 사용하는 템플릿 시스템을 사용하는지와 무관합니다.

URL 설계에서의 느슨한 결합 : Django 앱의 URL은 하부 Python 코드와 결합되어서는 안 됩니다.   
View 설계에서의 느슨한 결합 : 뷰는 개발자가 어느 템플릿 시스템을 사용하는지, 혹은 템플릿 시스템을 사용하는지에 무관해야 합니다.

따라서 저희의 투표앱인 polls에서도 상위 계층에서 예외를 한 번에 처리하거나 모델 API에서 Http404를 발생시키도록 할 수 있지만, 그렇게 한다면 model과 view가 서로 큰 연관성을 지니게 되므로 장고의 주요 디자인 목표 중 하나인 느슨한 결합을 유지하는 것을 어렵게 합니다. 따라서 저희는 view에서 발생한 http404 오류는 view에서 처리할 수 있도록 예외를 발생시키게 한 것 입니다.


## POST 방식과 GET 방식의 차이
이번 투표앱을 만들면서 HTML 파일의 form태그를 이용해 views.py로 POST 방식을 이용해 사용자가 투표한 내용을 보내는 코드를 작성한 적이 있습니다. 
장고 튜토리얼에서는 method를 get이 아닌 post로 사용해야하는 것은 중요하다라고 이야기 합니다. 그러면 get과 post 방식의 차이는 무엇이고 왜 투표앱에서는 post 방식을 사용해야 할까요?

##### get request
get 요청은 URL을 통해 데이터를 전송하며, 클라이언트에서 서버로 정보를 요청하기 위해 사용되는 메서드입니다. 
GET 요청은 URL의 끝에 쿼리스트링(query string)을 붙여서 데이터를 전송합니다. 쿼리스트링은 ?으로 시작하며, key=value 형태로 구성됩니다. 여러 개의 키-값 쌍을 전송할 때는 &로 구분합니다.

유튜브에서 영상을 검색하게 되면 get 요청을 통해 영상을 검색하는 것을 확인할 수 있습니다. 저번 파이썬 세션에서 유튜브 분석 api를 만들었을 때 영상의 id를 가지고 오기 위해 유튜브의 주소에서 id를 찾은 것을 생각해보면 get 요청이 url에 데이터를 담는다는 의미를 쉽게 이해하실 수 있을 것이라고 생각합니다.

추가적으로 get은
* 캐싱할 수 있습니다
* 브라우저 기록에 남습니다
* 북마크에 추가할 수 있습니다
* 데이터 길이에 대한 제한이 있습니다.

>캐싱이란?
>클라이언트가 웹 서버에 한번 페이지에 접근 후 해당 페이지를 또 요청할 시 빠르게 접근하기 위해 방문시 요청한 데이터를 저장해 두고 동일한 요청을 할 때 사용하여 서버에 대한 요청을 줄이기 위해 사용하는 방식

##### post request
POST 요청은 HTTP 메시지의 body라고 불리는 공간에 데이터를 넣고 전송하며 리소스를 생성/업데이트하기 위해 서버에 데이터를 보내는 데 사용합니다.
예를 들어, 로그인 폼을 작성하고 제출할 때 POST 요청을 사용합니다. POST 요청은 데이터를 서버에 제출하는 요청으로, 서버는 이에 대한 처리를 하고 결과를 반환합니다. 
POST 요청은 데이터의 길이에 제한이 없고, URL에 데이터가 노출되지 않으므로 get보다 보안 면에서 안전합니다. 따라서 데이터를 서버에 제출하고나, 상태를 변경할 때 사용됩니다. 예를 들어 로그인 정보 제출 (로그인 정보가 url에서 표시되면 안되므로), 게시글 작성(대용량 데이터를 전송) 이 있습니다.
> ##### post방식이라고 무조건 보안면에서 믿지 말아야 하는 이유!
> post 방식이 get방식보다 보안면에서 우수한 것은 맞지만, post 요청으로 전송한 데이터도 결국 크롬 개발자 도구같은 툴로 요청 내용을 확인 할 수 있기 때문에 민감한 비밀번호 같은 데이터들은 꼭 암호화를 해주어야 합니다.

##### 비교 정리표
<table style="border-collapse:collapse" border="1"> 
    <tr>
        <td> HTTP Method </td>
        <td> GET 방식 </td>
        <td> POST 방식 </td>
    </tr>
    <tr>
        <td> 사용 목적 </td>
        <td> 서버의 리소스에서 데이터를 요청하기 위함 </td>
        <td> 서버의 리소스를 새로 생성하거나 갱신하기 위함 </td>
    </tr>
    <tr>
        <td> 데이터가 담기는 곳 </td>
        <td> HTTP 패킷 Header </td>
        <td> HTTP 패킷 Body </td>
    </tr>
    <tr>
        <td> 리소스 전달 방식 </td>
        <td> 쿼리스트링 </td>
        <td> HTTP Body </td>
    </tr>
    <tr>
        <td> 캐싱 가능 여부 </td>
        <td> O </td>
        <td> X </td>
    </tr>
    <tr>
        <td> 브라우저 기록 </td>
        <td> O </td>
        <td> X </td>
    </tr>
    <tr>
        <td> 데이터 길이 제한 </td>
        <td> O </td>
        <td> X </td>
    </tr>

    
</table>

## 함수형 뷰와 클래스형 뷰
투표 앱을 작성하며 처음에는 index, detail, result를 view 함수를 이용해 작성하였지만, 나중에 더 편리하게 이용하기 위해 class IndexView, class DetailView, class ResultView 등의 제네릭뷰를 사용하여 수정하였습니다.
이처럼 def를 이용해 작성한 view 함수를 함수형 뷰, 제네릭뷰 처럼 클래스를 이용한 뷰를 클래스형 뷰라고 합니다. 둘은 어떻게 다를까요?

### 함수형 뷰
신속하고 간단한 개발이 가능하며 읽기 쉽지만, 로직이 복잡해질 수 있습니다.
또한 함수형 뷰에서는 일일이 post인지, get인지 확인해봐야한다는 단점이 있고, 코드를 확장하고 재사용하기 어렵습니다.
### 클래스형 뷰
웹 애플리케이션을 개발하는 경우, 공통적으로 반복되는 과정들이 많이 발생합니다. 장고에서는 특히 모델, 뷰, 템플릿 개발과정에서의 이러한 단순 반복 작업을 많이 없애주었는데, 제네릭뷰가 바로 뷰 개발과정에서 개발자의 단순 반복 작업을 덜어주는 기능입니다. 
즉, 제네릭 뷰란, 뷰 개발 과정에서 공통적으로 사용할 수 있는 기능들을 추상화하고, 이를 장고에서 미리 만들어 기본적으로 제공해주는 클래스형 뷰를 말합니다.
따라서 클래스형 뷰는 쉽게 확장하고 재사용이 가능하며, 별도의 클래스 메소드로 HTTP 메소드 처리가 가능합니다. 

하지만 함수형 뷰, 클래스형 뷰 각각의 장점과 단점이 있고 클래스형과 제너릭뷰가 무조건 좋다! 라고 하기에는 아직 의견이 분분한 점이 있기 때문에 코드를 작성하며 자신에게 맞는 뷰를 제작해야한다고 생각합니다.

****************************************************************************************************************************

# MVC 와 MTV



## 디자인패턴
소프트웨어를 설계할 때 특정 맥락에서 자주 발생하는 고질적인 문제들이 또 발생했을 때 재사용할 할 수있는 훌륭한 해결책
## MVC?
디자인 패턴 중 하나인 MVC패턴은 Model, View, Controller의 줄임말로 어플리케이션을 구성할 때 그 구성요소를 세가지의 역할을 구분한 패턴을 의미



![mvc](https://user-images.githubusercontent.com/69035864/235869685-3d5a3013-c538-40d9-9d94-2260338bfb3d.png)

Model : 데이터에 관련된 일(데이터를 처리하는 영역), 데이터베이스에서 데이터를 받아 전달

Controller : 모델과 뷰를 이어주는 중개자의 역할


    앱의 사용자로부터 입력에 대한 응답으로 모델 및 뷰를 업데이트 하는 로직을 포함
    사용자의 요청은 모두 컨트롤러를 통해 진행되어야 함
    컨트롤러로 들어온 요청은 어떻게 처리할지 결정하여 모델로 요청을 전달함

view : 사용자에게 보여지는 부분 담당(사용자한테 보이는 ui와 모델로부터 받은 데이터가 합쳐져 만들어진 화면)


## MVC를 지키는 방법

1. Model은 Controller와 View에 의존하지 않아야 한다.
(Model 내부에 Controller와 View에 관련된 코드가 있으면 안 된다.)


2. View는 Model에만 의존해야 하고, Controller에는 의존하면 안 된다.
(view 내부에 Model의 코드만 있을 수 있고, Controller의 코드가 있으면 안 된다.)

3. View가 Model로부터 데이터를 받을 때는, 사용자마다 다르게 보여주어야 하는 데이터에 대해서만 받아야 한다.

4. Controller는 Model과 View에 의존해도 된다.
(Controller 내부에는 Model과 View의 코드가 있을 수 있다.)

5. View가 Model로부터 데이터를 받을 때, 반드시 Controller에서 받아야 한다.

****

## django의 MTV 
![mvt](https://user-images.githubusercontent.com/69035864/235869623-277f1353-6168-40b2-81ed-384313a93a97.png)


Model = Model(MVC) : 데이터에 관련된 부분

    MVC 패턴의 모델에 대응되며 DB에 저장되는 데이터를 의미합니다. 모델은 클래스로 정의되며 하나의 클래스가 하나의 DB Table입니다.

    원래 DB를 조작하기 위해선 SQL을 다룰 줄 알아야 하지만 장고는 ORM(Object Relational Mapping)기능을 지원하기 때문에 파이썬 코드로 DB를 조작할 수 있습니다.

Template = View(MVC) : 사용자에게 보여지는 부분


    MVC 패턴의 뷰에 대응되며 유저에게 보여지는 화면을 의미합니다. 장고는 뷰에서 로직을 처리한 후 html 파일을 context와 함께 렌더링하는데 이 때의 html 파일을 템플릿이라 칭합니다.

    장고는 자체적인 Django Template 문법을 지원하며 이 문법 덕분에 html 파일 내에서 context로 받은 데이터를 활용할 수 있습니다.

View = Controller(MVC) : 웹 요청를 받고, 전달받은 데이터들을 해당 어플리케이션의 로직으로 가공하여, 그 결과를 템플릿에 보내준다. 

    MVC 패턴의 컨트롤러에 대응되며 요청에 따라 적절한 로직을 수행하여 결과를 템플릿으로 렌더링하며 응답합니다. 다만 항상 템플릿을 렌더링 하는 것은 아니고 백엔드에서 데이터만 주고 받는 경우도 있습니다.

### URLconf(URL 설계)

URL은 view와 template을 이어주는 역할, 이 부분을 만들어 주는 작업을 URLconf라고 한다. path함수를 사용.

URL 패턴을 정의하여 해당 URL과 뷰를 매핑하는 단계

# HTTP Method 

클라이언트와 서버 사이에 이루어지는 요청(Request)과 응답(Response) 데이터를 전송하는 방식을 말한다.

-서버에 주어진 리소스에 수행하길 원하는 행동, 서버가 수행해야 할 동작을 지정하는 요청을 보내는 방법이다.

## 주요 메소드
GET: 리소스 조회

POST: 요청 데이터 처리, 주로 등록에 사용

PUT : 리소스를 대체(덮어쓰기), 해당 리소스가 없으면 생성

PATCH : 리소스 부분 변경(PUT이 전체 변경, PATCH는 일부 변경)

DELETE : 리소스 삭제



# PK란?

Primary key - model의 기본 키를 나타냅니다.

각각의 모델 인스턴스는 데이터베이스 테이블에서 행으로 저장되는데,각각의 행은 고유한 식별자(primary key)를 갖고 있어야 합니다. Django에서 모델을 정의할 때 기본적으로 id필드가 생성되며 이 id가 모델의 기본 키가 되지만 id 대신에 pk로 필드를 지정할 수 있습니다.


추가적으로 데이터베이스의 열에 저장되는 것은 모델에 포함되는 데이터의 속성인 필드라고 불리는 것입니다. 즉 각각의 필드는 모델이 가지는 데이터의 특성이나 정보를 나타냅니다. 예시를 들어서 저희가 만든 Question 모델에서의 question_text 핃드, pub_date 필드 등이 저장하는 게시된 날짜, 시간 정보등이 있습니다. 이외에도 장고에서는 다양한 종류의 필드를 제공합니다.


## pk와 id의 다른 점

id는 기본적으로 생성되며 자동으로 증가하는 정수 값을 가집니다. 또한 이름을 변경할 수 없습니다. 

pk는 필드를 정의할 때 직접 지정해주어야 하고, 필드의 이름을 변경할 수 있습니다. 또한 모델의 다른 필드와 이름이 충돌하지 않아야 합니다.


기본적으로 생성된 id를 Question.objects.get(id=1) 이런 방식으로 인스턴스를 가지고 오는 방법도 있지만 Question.objects.get(pk=1) 이렇게 pk를 이용해서 인스턴스를 가지고 올 수도 있다. 반대도 가능하다. 하지만 일반적으로 pk 필드를 사용할 때는 pk로 지정하여 사용하는 것이 가독성이 좋고, 모델의 다른 필드와 이름이 충돌하지 않기 때문에 안전하다.

## polls에서 pk를 사용한 예시

DetailView 제너릭 뷰는 URL에서 캡처된 기본 키 값이 "pk"라고 기대하기 때문에 question_id를 제너릭 뷰를 위해 pk로 변경합니다.
get() 메서드는 기본적으로 키워드 인자로서 모델의 필드를 지정하여 객체를 검색합니다. 

예를 들어, Question 모델에서 id가 1인 객체를 가져오려면 Question.objects.get(id=1)와 같이 사용할 수 있습니다.


# 캐시(cache)와 쿠키(cookie)

모두 웹 브라우저에서 웹사이트를 이용할 때 중요한 역할을 하는 요소


## 캐시(cache)는 
웹 브라우저가 이전에 방문한 웹사이트의 정보를 저장해놓는 임시 저장소입니다. 이렇게 저장해놓으면 웹 브라우저는 이전에 방문한 웹사이트를 다시 방문할 때마다 웹사이트의 정보를 서버에서 다시 받아와서 표시하는 것이 아니라, 저장된 정보를 이용하여 더 빠르게 웹사이트를 표시할 수 있습니다. 이렇게 캐시를 이용하면 웹사이트를 더 빠르고 효율적으로 이용할 수 있습니다.

## 쿠키(cookie)는 
웹사이트에서 사용자의 컴퓨터에 저장하는 작은 파일입니다. 쿠키는 사용자가 웹사이트를 방문할 때, 웹사이트에서 사용자의 컴퓨터에 저장되며, 사용자가 다시 웹사이트를 방문할 때마다 쿠키가 전송됩니다. 쿠키를 이용하여 사용자의 로그인 정보나, 사용자의 환경 설정 등을 저장할 수 있습니다.

따라서, 캐시와 쿠키는 둘 다 웹사이트 이용을 더 편리하고 빠르게 만들어주는 역할을 하지만, 캐시는 브라우저 측에, 쿠키는 서버 측에 저장됩니다. 또한, 캐시는 이전에 방문한 웹사이트의 정보를 저장하여 더 빠르게 표시할 수 있게 해주지만, 쿠키는 사용자의 정보를 저장하여 웹사이트 이용을 편리하게 해줍니다.

