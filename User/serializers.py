from rest_framework import serializers
from .models import User, Clients

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"

class ClientGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('email', )