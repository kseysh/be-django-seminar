from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from rest_framework.views import APIView
from .serializers import PostListModelSerializer, PostRetrieveModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,status

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer


class PostListCreateView(generics.ListAPIView,generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user.is_authenticated:
            serializer.save(writer=request.user)
        else:
            serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostRetrieveUpdateView(generics.RetrieveAPIView,generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveModelSerializer


@api_view()
def calculator(request):
    num1 = request.GET.get('num1',0)
    num2 = request.GET.get('num2',0)
    operators = request.GET.get('operators')

    result = int(num1) + int(num2)

    data={
        'type':'FBV',
        'result':result,
    }

    return Response(data)

class CalculatorAPIView(APIView):
    def get(self, request):
        num1 = request.GET.get('num1',0)
        num2 = request.GET.get('num2',0)
        result = int(num1) + int(num2)

        data={
            'type':'CBV',
            'method':'POST',
            'result':result,
        }
        return(data)
    def post(self, request):
        data={
            'type':'CBV',
            'method':'POST',
            'result':0,
        }
        return Response(data)

        