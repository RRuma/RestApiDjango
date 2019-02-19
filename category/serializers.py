from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category

# title = serializers.CharField(max_length=120)
# description = serializers.CharField()
# body = serializers.CharField()
#
#
# # author_id = serializers.IntegerField()
#
# def create(self, validated_data):
#     return Category.objects.create(**validated_data)

# class categoryUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id")


class categorySerializer(serializers.ModelSerializer):
    #user = categoryUserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ( "categoryname", "description")