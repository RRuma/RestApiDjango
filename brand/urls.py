from django.urls import path

from .views import BrandDetailAPIView,BrandListAPIView,BrandCreateAPIView,BrandDeleteAPIView,BrandUpdateAPIView

app_name = "category"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    #path('articles/',ArticleView.as_view()),
    path('',BrandListAPIView.as_view(),name = "list"),
    path('create/',BrandCreateAPIView.as_view(),name = "create"),
    path('detail/<int:pk>/',BrandDetailAPIView.as_view(),name = "detail"),
    path('update/<int:pk>/',BrandUpdateAPIView.as_view(),name = "update"),
    path('delete/<int:pk>/',BrandDeleteAPIView.as_view(),name = "delete"),

    #path('list/',BrandDeleteAPIView.as_view(),name = "detail"),

]