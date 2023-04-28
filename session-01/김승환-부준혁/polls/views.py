from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     #출판일자를 정렬하여 5개까지만 가지고 온다.
#     #template = loader.get_template("polls/index.html")
#     context = {"latest_question_list":latest_question_list}
    
#     #output = ", ".join([q.question_text for q in latest_question_list])
#     #.join함수를 이용하여 5개를 콤마를 이용해 구분
#     return render(request, "polls/index.html",context)
#     #render는 request 객체를 첫번째 인수로 받고, 템플릿 이름을 두 번째 인수로 받으며,
#     #context 사전형 객체를 선택적 인수로 받는다. 
#     # 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환된다.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    #request마다 order_by가 실행된다.
    #queryset = Qusetion.~~ 이처럼 쓰면 앱이 시작될 때 단 한 번만 함수가 실행된다.
    
# 클래스 형 뷰는 기본적으로 클래스로 진입하기 위한 as_view() 클래스 메소드를 제공합니다. 
# as_view( ) 진입 메소드의 역할은 클래스의 인스턴스를 생성하고, 그 인스턴스의 dispath( ) 메소드를 호출합니다. 
# dispath( ) 메소드는 요청을 검사해서 GET, POST 등의 어떤 HTTP 메소드로 요청되었는지를 알아낸 다음, 
# 인스턴스 내에서 해당 이름을 갖는 메소드로 요청을 중계해줍니다.


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Questio n does not exist")
#     return render(request, "polls/detail.html", {"question": question})
# 예외처리를 통해 404 error를 발생시키는 방법

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

#get()을 사용해 Http404 예외를 발생시키는 방법
# get_object_or_404는 Django 객체를 첫 번째 인자로 받고, 
# 몇개의 키워드 인수를 모델 관리자의 get()함수에 넘긴다. 
# 만약 객체가 존재하지 않는다면, 404에러를 발생시킨다
#pk : primary key의 약어로 데이터베이스 테이블의 각 행을 고유하게 식별하는 유일한 값

class DetailView(generic.DetailView):
    #URL에서 캡처된 기본 키 값이 pk라고 기대하기 때문에 question_id를 pk로 변경한 것 임
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())




class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
#filter() 함수는 모델 클래스의 인스턴스들 중에서 특정 조건에 맞는 객체들만을 추출해내는데 사용됩니다.

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        #request.POST => 키로 전송된 자료에 접근할 수 있도록 해주는 객체
        # POST로 전달되는 key값인 choice는 detail.html에서 form으로 전달된 input의 name값이다.
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        #reverse 함수는 URL 패턴 이름을 사용하여 URL을 역으로 검색(reverse)하는 함수입니다.
        #POST방식은 HttpResponseRedirect를 사용하여 반환해야한다.
        #"polls" 애플리케이션의 "results" 뷰와 관련된 URL 패턴을 찾고 
        # 해당 패턴에서 question.id 값이 매개 변수로 전달되도록 URL 문자열을 생성합니다.
        #reverse() 함수를 사용하면 URL 패턴을 변경하더라도 이전 URL을 사용하는 뷰 함수가 있는 경우 
        # 코드를 수정할 필요 없이 URL 패턴 이름만 수정하면 되므로, 
        # Django 애플리케이션의 유지 보수성과 재사용성을 높일 수 있습니다.

        #예를 들어, "polls:results" URL 패턴의 이름이 "results"라고 정의되어 있다면 reverse("polls:results") 함수를 호출하여 해당 URL을 역으로 검색할 수 있습니다.
        #추가로, URL 패턴 이름 뿐만 아니라, 위치 인수(args)와 키워드 인수(kwargs)를 전달하여 URL 패턴에서 요구하는 동적 매개변수를 지정할 수도 있습니다. 
        # 예를 들어, reverse("polls:results", args=(question.id,))는 "polls:results" 패턴에 question.id를 인자로 전달하여 해당 URL을 역으로 검색할 수 있습니다.


# # Django의 views.py 파일은 웹 어플리케이션의 요청(request)을 처리하고, 
# # 적절한 HTTP 응답(response)또는 예외를 반환하는 함수들을 포함합니다.
# # HttpResponse는 Django에서 가장 기본적인 HTTP 응답 객체 중 하나입니다. 
# # 이 객체를 사용하면, 단순한 문자열, HTML 코드, JSON 데이터 등을 포함한 응답을 생성할 수 있습니다.


# loader는 템플릿을 로드하기 위해 사용되는 객체입니다. 
# 일반적으로 loader.get_template() 메서드를 사용하여 템플릿 파일을 로드하고, 
# 그 결과로 Template 객체를 반환합니다. 
# 이후에는 Template 객체의 render() 메서드를 사용하여 컨텍스트를 적용한 렌더링 결과를 생성할 수 있습니다.

# render는 Django에서 매우 일반적으로 사용되는 단축 함수입니다. 
# render() 함수는 loader를 사용하여 템플릿을 로드하고 컨텍스트를 적용한 후, 
# HttpResponse 객체를 반환합니다. 따라서 템플릿 파일을 로드하고 렌더링하는 작업을 한 번에 처리할 수 있습니다.

# 따라서, loader는 템플릿을 로드하기 위한 객체이고, 
# render는 템플릿 파일을 로드하고 컨텍스트를 적용한 뒤 HttpResponse 객체를 반환하는 간단한 방법입니다. 
# render는 코드를 간결하게 만들어줍니다.
