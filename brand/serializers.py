from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Brand

class brandSerializer(serializers.ModelSerializer):
    #user = categoryUserSerializer(read_only=True)

    class Meta:
        model = Brand
        fields = ( "brandName", "description")