from rest_framework import serializers
from .loginfile import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'