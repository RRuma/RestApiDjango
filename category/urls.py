from django.urls import path
from django.conf.urls import url

from .views import CategoryDetailAPIView,CategoryListAPIView,CategoryCreateAPIView,CategoryUpdateAPIView,CategoryDeleteAPIView,CategoryDestroyAPIView

app_name = "category"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    #path('articles/',ArticleView.as_view()),
    #url(r'^cat/', include('category.urls')),
    path('',CategoryListAPIView.as_view(),name = "list"),
    path('create/',CategoryCreateAPIView.as_view(),name = "create"),
    path('detail/<int:pk>/',CategoryDetailAPIView.as_view(),name = "detail"),
    path('update/<int:pk>/',CategoryUpdateAPIView.as_view(),name = "update"),
    path('delete/<int:pk>/',CategoryDeleteAPIView.as_view(),name = "delete"),

    #url(r'^', CategoryListCreateAPIView.as_view(),name = "list"),
    #url(r'^/(?P<pk>[0-9]{4})/$',CategoryDetailAPIView.as_view(),name = "detail"),

    #url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive)
    #path('articles/<int:year>/', views.year_archive)
    #url(r'^$', views.homepage),
]