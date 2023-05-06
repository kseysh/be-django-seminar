from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
# 커뮤니티 게시판 

class Post(models.Model):
    # image = models.ImageField(verbose_name='이미지') # 게시글 이미지 저장 필드  -- 이미지는 일단 보류
    
    content = models.TextField('내용') # 게시글 내용 저장 필드 
    created_at = models.DateTimeField('작성일') # 작성 시간
    view_count = models.IntegerField('조회수')  # 조회수   

# 댓글 모델

#class Comment(models.Model)

#안녕