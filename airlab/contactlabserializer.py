from rest_framework import serializers
from .contactlabmodels import ContactLab

class ContactLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactLab
        fields = '__all__'