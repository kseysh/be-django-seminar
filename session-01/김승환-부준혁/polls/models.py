import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #질문의 데이터형은 문자, 최대 200자까지 사용 가능
    #CharField는 max_length가 필수 인수이다.
    pub_date = models.DateTimeField("date published")
    # 
    def __str__(self):
        return self.question_text
    #객체가 문자열로 변환될 때 self.question_text를 반환함
    @admin.display(
    #admin 모듈에서 제공하는 데코레이터
    boolean=True,
    # true, false 값을 표시하도록 함
    ordering="pub_date",
    #pub_date를 기준으로 정렬하도록 함
    description="Published recently?",
    # 필드의 설명 설정
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey => Question이라는 외부 model을 참조하겠다.
    #  on_delete=models.CASCADE => Question이 삭제되면 Choice에 있는 Question도 삭제하겠다.
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # 투표 , 기본값을 0으로 설정
    def __str__(self):
        return self.Choice_text

    