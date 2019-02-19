from django.urls import path

from .views import TodoListCreateAPIView, TodoDetailAPIView

app_name = "articles"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    #path('articles/',ArticleView.as_view()),
    path('',TodoListCreateAPIView.as_view(),name = "list"),
    path('<int:pk>/',TodoDetailAPIView.as_view(),name = "detail"),
]