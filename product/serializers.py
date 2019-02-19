from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category,Product,Brand


# class categorySerializer(serializers.ModelSerializer):
#     #user = categoryUserSerializer(read_only=True)
#
#     class Meta:
#         model = Category
#         fields = ( "categoryname", "description")


class productCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("categoryname", "description")


class productBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("brandName", "description")

    # def to_representation(self, instance):
    #     self.fields['brand'] = productBrandSerializer(read_only=True)
    #     return super().to_representation(instance)




class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ( "productName", "productPrice", "description", "category","brand") # fields from product model + foreign keys

    def to_representation(self, instance):
        self.fields['category'] = productCategorySerializer(read_only=True)
        self.fields['brand'] = productBrandSerializer(read_only=True)
        return super().to_representation(instance)

    # def to_representation(self, instance):
    #     self.fields['brand'] = productBrandSerializer(read_only=True)
    #     return super().to_representation(instance)