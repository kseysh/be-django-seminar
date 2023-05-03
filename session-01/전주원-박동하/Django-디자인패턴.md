# Django의 디자인 패턴

### 📜 Django란?
**MVC 패턴**를 기반으로 한 **MTV 패턴**이 적용된 웹 **프레임워크**

>#### 프레임워크란?
>소프트웨어의 설계와 구현을 **재사용**이 가능하도록 일련의 협업화된 형태로 클래스들을 제공하는 것
>* 회원가입, 로그인/로그아웃 등 사용자 정보를 다루는 기능에 대한 클래스
>* 백엔드에서 움직이는 데이터를 처리하고 저장하는 방식에 대한 클래스

### 🧩 디자인 패턴이란?
소프트웨어 개발 중 **자주 발생하는 문제를 해결**하기 위해 방법을 패턴화한 설계의 원칙

#

### 🧩 MVC 패턴이란?
`Model` `View` `Controller`로 구성된 소프트웨어 개발의 디자인 패턴 중 하나로, 애플리케이션을 세 가지의 역할로 구분한 개발 방법론

&rarr; 유지보수성 · 확장성 · 유연성 증가, 중복 코딩의 문제 해결

![MVC 패턴](https://user-images.githubusercontent.com/97721883/235830787-0a8ddb11-6b08-4d6e-815e-d52ac487157b.PNG)

#### Model
* 데이터와 상호작용
* Django의 `Model`에 정의된 1개의 class = DB의 1개의 table
* `View`나 `Controller`의 정보 포함하면 안됨

#### View
* 사용자 인터페이스 담당
* 데이터 입력/출력/전달하는 역할
* `View` 자체에 데이터가 저장되어서는 안됨

#### Controller
* `Model`과 `View` 연결
* 사용자의 모든 행동을 처리, 로직 수행하는 역할
* `Model` `View`와 달리 사용자의 정보 모두 포함

<br>

>#### MVC 패턴을 웹에 적용하면?
>1. 사용자가 웹사이트에 접속 &rarr; **Uses**
>2. `Controller`는 사용자가 요청한 웹사이트를 서비스하기 위해 `Model` 호출 &rarr; **Manipulates**
>3. `Model`은 DB나 파일과 같은 데이터 소스를 제어한 후 그 결과를 리턴
>4. `Controller`는 `Model`이 리턴한 결과를 `View`에 반영 &rarr; **Updates**
>5. 데이터가 반영된 `View`가 사용자에게 보여짐 &rarr; **Sees**

#

### 🧩 MTV 패턴이란?
`Model` `Template` `View` + `URLconf`로 MVC에 대응되는 Django의 디자인 패턴

![MTV 패턴](https://user-images.githubusercontent.com/97721883/235831075-7cfb4879-9a1f-46c1-a7de-69d923464ebd.PNG)

#### Model
* MVC 패턴의 `Model`에 대응
* Django의 `Model`에 정의된 1개의 class = DB의 1개의 table
* Django는 ORM(Object Relational Mapping) 기능을 지원하기 때문에 python 코드로 DB 조작 가능

#### Template
* MVC 패턴의 `View`에 대응
* Django는 `View`에서 로직 처리한 후 html 파일을 context와 함께 렌더링, 여기서 html 파일이 `Template`
* Django의 자체적인 Django Template 문법 덕분에 html 파일 내에서 context로 받은 데이터 활용 가능

#### View
* MVC 패턴의 `Controller`에 대응
* 요청에 따른 적절한 로직을 수행하여 결과를 `Template`으로 렌더링하며 응답
* `Template`으로 렌더링하거나 백엔드에서 데이터만 주고받기도 함

#### URLconf
* 장고만의 차이점
* URL 패턴을 정의하여 해당 URL과 `View`를 매핑

---

##### 💡 Summary

<table border=1 style="border-collapse: collapse;">
  <tr>
    <th></th>
    <th>MVC</th>
    <th>MTV</th>
  </tr>
  <tr>
    <td>데이터와 상호작용</td>
    <td>Model</td>
    <td>Model</td>
  </tr>
  <tr>
    <td>사용자 인터페이스</td>
    <td>View</td>
    <td>Template</td>
  </tr>
  <tr>
    <td>데이터와 사용자 인터페이스 연결</td>
    <td>Controller</td>
    <td>View</td>
  </tr>
</table>

![Django 디자인 패턴](https://user-images.githubusercontent.com/97721883/235831177-891da75b-2738-416d-ae1c-37d214e91d68.PNG)
