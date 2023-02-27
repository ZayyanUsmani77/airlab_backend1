from rest_framework import serializers
from .labimagemodels import LabImage

class LabImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabImage
        fields = '__all__'