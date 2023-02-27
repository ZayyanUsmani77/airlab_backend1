from rest_framework import serializers
from .labmodels import Lab

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'