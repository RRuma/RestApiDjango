
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from .models import Product
from django.db.models import Q

from .serializers import productSerializer
#from .permissions import UserIsOwnerTodo

# Create your views here.
class ProductListAPIView(ListAPIView):
    serializer_class = productSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('productName', 'productPrice', 'category__categoryname', 'brand__brandName')  # for other tables use model__field

    def get_queryset(self):
        search = self.request.query_params.get("search")
        print("name : "+str(search))
        if search:
            return Product.objects.filter(Q(productName__contains=search) | Q(productPrice__contains=search) | Q(category__categoryname__contains=search) | Q(brand__brandName__contains=search))
            #return Product.objects.filter(Q(productName__contains=search)| Q(productPrice__contains=search)|Q(category__categoryname__contains=search)|Q(brand__brandName__cotains = search))
        else:
            return Product.objects.all()


class ProductCreateAPIView(CreateAPIView):
    serializer_class = productSerializer

    def perform_create(self,serializer):
       #return Category.objects.create()
       serializer.save()

class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = productSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = productSerializer
    queryset = Product.objects.all()

class ProductDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = productSerializer
    queryset = Product.objects.all()

class CategoryDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = productSerializer
    queryset = Product.objects.all()
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
