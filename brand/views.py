from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView, RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from .models import Brand
from django.db.models import Q

from .serializers import brandSerializer
#from .permissions import UserIsOwnerTodo


# Create your views here.
class BrandCreateAPIView(CreateAPIView):
    serializer_class = brandSerializer

    def perform_create(self, serializer):
        serializer.save()

class BrandListAPIView(ListAPIView):
    serializer_class = brandSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('brandName', 'description')

    def get_queryset(self):
        search = self.request.query_params.get("search")
        print("name : " + str(search))
        if search:
            return Brand.objects.filter(Q(brandName__contains=search))
            # return Product.objects.filter(Q(productName__contains=search)| Q(productPrice__contains=search)|Q(category__categoryname__contains=search)|Q(brand__brandName__cotains = search))
        else:
            return Brand.objects.all()


class BrandDetailAPIView(RetrieveAPIView):
    serializer_class = brandSerializer
    queryset = Brand.objects.all()

class BrandUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = brandSerializer
    queryset = Brand.objects.all()

class BrandDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = brandSerializer
    queryset = Brand.objects.all()

class BrandDeleteAPIView3(RetrieveUpdateDestroyAPIView):
    serializer_class = brandSerializer
    queryset = Brand.objects.all()
        # else:
        #     return Brand.objects.all()


    #def get_queryset(self):
        #return Brand.objects.all()

    # def get_queryset(self):
    #     name = self.request.query_params.get("brand1")
    #     print("brandName : " + str(name))
    #     if name:
    #         return Brand.objects.filter(Q(brandName__contains=name))

# class BrandListCreateAPIView(ListCreateAPIView):
#     serializer_class = brandSerializer
#
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('brandName', 'description')
#
#     def get_queryset(self):
#         #return Category.objects.filter(user=self.request.user)
#         return Brand.objects.all()
#
#     def perform_create(self,serializer):
#        #return Category.objects.create()
#        serializer.save()

# class BrandDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = brandSerializer
#     queryset = Brand.objects.all()



