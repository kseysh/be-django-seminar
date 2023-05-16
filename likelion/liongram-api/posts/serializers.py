from rest_framework.serializers import ModelSerializer

from .models import Post,Comment

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'id',
            'image',
            'created_at',
            'view_count',
            'writer',
        ]
        depth = 1


class PostRetrieveModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        depth = 1


class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = [
            'image',
            'created_at',
            'view_count',
            'writer',
        ]
        depth = 1

class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields ='__all__'

