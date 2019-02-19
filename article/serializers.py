from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo


class TodoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")

class TodoSerializer(serializers.ModelSerializer):
    user = TodoUserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ("user", "name", "done", "date_created")

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()