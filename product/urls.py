from django.urls import path

from .views import ProductDetailAPIView,ProductCreateAPIView,ProductListAPIView,ProductDeleteAPIView,ProductUpdateAPIView

app_name = "category"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    #path('articles/',ArticleView.as_view()),
    path('',ProductListAPIView.as_view(),name = "list"),
    path('create/',ProductCreateAPIView.as_view(),name = "create"),
    path('detail/<int:pk>/',ProductDetailAPIView.as_view(),name = "detail"),
    path('update/<int:pk>/',ProductUpdateAPIView.as_view(),name = "update"),
    path('delete/<int:pk>/',ProductDeleteAPIView.as_view(),name = "delete"),
    #path('list/',ProductDetailAPIView.as_view(),name = "detail"),
]