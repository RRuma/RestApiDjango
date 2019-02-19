from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response

from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import generics


from .models import Category
from django.db.models import Q

from .serializers import categorySerializer
from .permissions import UserIsOwnerTodo

# Create your views here.
class CategoryListAPIView(ListAPIView):
    serializer_class = categorySerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('categoryname', 'description')

    def get_queryset(self):
        search = self.request.query_params.get("search")
        print("name : " + str(search))
        if search:
            return Category.objects.filter(Q(categoryname__contains=search))
            # return Product.objects.filter(Q(productName__contains=search)| Q(productPrice__contains=search)|Q(category__categoryname__contains=search)|Q(brand__brandName__cotains = search))
        else:
            return Category.objects.all()

class CategoryCreateAPIView(CreateAPIView):
    serializer_class = categorySerializer

    def perform_create(self,serializer):
       #return Category.objects.create()
       serializer.save()


class CategoryDetailAPIView(RetrieveAPIView):
    serializer_class = categorySerializer
    queryset = Category.objects.all()

class CategoryUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializer
    lookup_field = 'pk'

class CategoryDeleteAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = categorySerializer
    lookup_field = 'pk'

class CategoryDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = categorySerializer
    queryset = Category.objects.all()

   # permission_classes = (IsAuthenticated, UserIsOwnerTodo)

    # def update(self, instance, validated_data):
    #     #queryset = Category.objects.all()
    #     instance.categoryname = validated_data.get('categoryname', instance.categoryname)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance

    # def delete(self, request, pk):
    #     # Get object with this pk
    #     article = get_object_or_404(Category.objects.all(), pk=pk)
    #     article.delete()
    #     return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)
