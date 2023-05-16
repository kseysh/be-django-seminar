"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    #만약 주소중에 polls/가 보이면 뒤 문자열을 파싱해서 polls.urls로 연결시켜준다.
    path('admin/', admin.site.urls),
]

# urlpatterns는 URL 패턴과 URL과 매핑될 view 함수를 정의하는 리스트.
# 위 코드에서는 /polls/로 시작하는 URL 요청은 polls 앱의 urls.py 파일에서 정의한 URL 패턴과 매핑된다.

# include() 함수는 다른 URL 패턴 정의를 가져올 때 사용. 
# include 함수는 다른 URL 패턴을 포함할 때마다 항상 사용. admin.site.urls가 유일한 예외.
# path() 함수는 URL 패턴과 매핑될 view 함수를 설정. 

# 마지막으로, /admin/으로 시작하는 URL 요청은 Django의 기본 관리자 사이트에 매핑됩니다. 
# 이를 처리할 view 함수는 django.contrib.admin 앱의 site 객체에 정의되어 있습니다.