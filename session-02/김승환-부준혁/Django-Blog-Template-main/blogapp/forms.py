from dataclasses import fields
from msilib.schema import File
from django import forms
from .models import Blog

# 모델이 나중에 결정됨 (views.py 의 메소드 실행시에) => 어떤 모델을 기반으로 form 을 만들지 결정되어 있지 않음
class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget = forms.Textarea)

# 모델이 현재 바로 이미 결정됨 => 애초에 form 의 존재가 모델을 기반으로 함
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'body']
