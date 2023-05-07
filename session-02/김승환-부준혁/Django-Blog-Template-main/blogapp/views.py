from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone



from .models import Post,Comment
User = get_user_model()


def home(request):
    return render(request, 'index.html')

@login_required
def new(request):
    if request.method=='GET':
        return render(request, 'new.html')
    else:        
        title = request.POST.get('title')
        body = request.POST.get('body')
        print(title)
        print(body)
        Post.objects.create(
            headline = title,
            content = body
        )
        return HttpResponseRedirect('/community')

def login(request):
    if request.method=='POST':
        return HttpResponseRedirect('/mbtitest')
    else:
        return render(request,'login.html')

def community(request):
    post_list = Post.objects.all()
    context = {"post_list":post_list}
    return render(request,'community.html',context)

def newuser(request):
    if request.method=='POST':
        return render(request,'index.html')
    else:
        return render(request,'newuser.html')

@login_required
def mbtitest(request):
    if request.method=='POST':
        return HttpResponseRedirect('/community')
    else:
        return render(request,'mbtitest.html')
#리다이렉션이란 웹 브라우저에서 요청한 url을 다른 url로 변경하여 새로운 페이지로 이동시키는 기능
# 웹 애플리케이션에서 리다이렉션을 사용하는 경우
# 1. 사용자가 요청한 페이지를 삭제한 경우
# 2. 사용자가 요청한 페이지의 URL이 변경된 경우
# 3. 사용자가 로그인 또는 로그아웃 등의 작업을 수행한 후, 
#    이전 페이지로 다시 이동시키기 위한 경우

# HttpResponseRedirect를 사용할 때, 인자로 전달하는 URL은 반드시 절대 경로여야 한다.
# 따라서, 'communty' 대신 '/communty'로 변경하여야
# 원하는 URL로 리다이렉션이 가능하다.

def detail(request,post_id):
        post = get_object_or_404(Post, pk = post_id)
        if request.method=='GET':
            context = {"post":post,}
            return render(request,"detail.html",context)
        else:
            comment_text = request.POST.get('comment_text')
            user_id = request.POST.get('user_id')
            writer = get_object_or_404(User, pk=user_id)
            created_at = timezone.now()
            Comment.objects.create(
            content = comment_text,
            #writer = writer,
            writer = request.user,
            created_at = created_at,
            post = post
            )
            return HttpResponseRedirect(reverse("detail", args=(post_id,)))



def edit(request,post_id):
    if request.method=='POST':
        return HttpResponseRedirect(reverse("detail", args=(post_id,)))

    else:
        return render(request,'edit.html')

