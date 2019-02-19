from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .permissions import UserIsOwnerTodo
from .serializers import ArticleSerializer,TodoSerializer

# Create your views here.

class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerTodo)


# class ArticleView(APIView):
#     def get(self,request):
#         articles = Article.objects.all()
#         # the many param informs the serializer that it will be serializing more than a single article.
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({"articles": serializer.data})
