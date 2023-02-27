from rest_framework import serializers
from .booklabmodels import BookLab

class BookLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLab
        fields = '__all__'