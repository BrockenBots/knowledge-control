from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import *


class UserResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResult
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'