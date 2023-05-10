from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    #ChoiceInline은 Question 모델에서 Choice 모델을 조작하기 위한 Inline Form을 생성하는데 사용된다.
    model = Choice
    #model은 ChoiceInline에서 사용할 모델을 지정합니다.
    extra = 3
    #extra는 추가할 form 수를 지정합니다.


class QuestionAdmin(admin.ModelAdmin):
    # QuestionAdmin은 admin.py 파일에서
    # Question 모델의 관리자 페이지를 커스터마이징하기 위한 클래스입니다. 
    fieldsets = [
        #관리자 페이지에서 모델 객체를 표시할 때 필드들을 그룹으로 묶어서 표시하고 싶을 때 사용
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
         #fieldsets의 각 튜플의 첫 번째 요소는 fieldset의 제목이다.
    ]
    inlines = [ChoiceInline]
    # 1:N 관계를 가지는 다른 모델 객체를 함께 편집하고 싶을 때 사용
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # 관리자 페이지의 객체 리스트 화면에서 보여질 필드 이름들을 지정
    list_filter = ["pub_date"]
    # 관리자 페이지에서 특정 필드에 대한 필터 기능을 사용할 수 있도록 함
    search_fields = ["question_text"]
    # 관리자 페이지에서 검색 기능을 사용할 수 있도록 함




admin.site.register(Question, QuestionAdmin)
# 관리 사이트에서 poll app을 변경가능하도록 만드는 기능
