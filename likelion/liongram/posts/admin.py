from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model=Comment
    extra=1


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=('id','writer','content','image','created_at','view_count')  
    #list_editable = ('content',)
    list_filter=['created_at']
    search_fields = ('id','writer__username')
    search_help_text = '게시판 번호, 작성자 검색이 가능합니다.'
    readonly_fields = ('created_at',)
    inlines = [CommentInline]

#admin.site.register(Comment)