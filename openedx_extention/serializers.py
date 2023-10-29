from rest_framework import serializers
from .models import *


class UserGreetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = '__all__'
