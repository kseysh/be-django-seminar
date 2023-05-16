from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Faq(models.Model):
    CATEGORY_ONE = '1'
    CATEGORY_TWO = '2'
    CATEGORY_THREE = '3'
    # 개발 원칙 : 의미가 불분명한 매직 넘버를 상수로 선언하라.
    CATEGORY_CHOICES =[
        (CATEGORY_ONE,'일반'),
        (CATEGORY_TWO,'계정'),
        (CATEGORY_THREE,'기타'),
    ]# 개발에서 사용하는 것은 1,2,3 사용자가 보는 것은 일반,계정,기타 를 본다.
    # 1,2,3 이나 알파벳을 통해 구분해야 이후 개발에서 외국에서 사용하거나, 개발시에 더 효율적으로 코딩이 가능하다.
    # 질문, 카테고리, 답변 생성자 생성일시 최종 수정자 최종수정일시
    title = models.CharField(verbose_name='제목',max_length=20)
    content = models.TextField(verbose_name='내용')
    category = models.CharField(verbose_name='카테고리',max_length=1, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(verbose_name='생성일시',null=True,default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='최종 수정일시',auto_now=True)
    # auto_now_add 처음 객체가 생성될 때만 변경
    # auto_now 객체가 저장될 때마다 변경
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name="faq_created_by")
    updated_by = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name="faq_updated_by")
    # related_name은 어떤 유저인지 구분하기 위함이다. 하지만 코드의 일관성을 위해 항상 작성하는 습관을 들인다.



class Answer(models.Model):
    content = models.TextField(verbose_name='답변 글')
    answered_by = models.ForeignKey(to=User,on_delete=models.CASCADE)
    answered_at = models.DateTimeField(verbose_name="답변일시",null=True,default=timezone.now)
    faq = models.ForeignKey(to=Faq,on_delete=models.CASCADE)