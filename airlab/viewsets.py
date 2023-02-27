from rest_framework import viewsets
from . import models
from . import serializers

class SignupViewset(viewsets.ModelViewSet):
    queryset = models.Signup.objects.all()
    serializer_class = serializers.SignupSerializer


#list() , retrive(), create() , update(), destroy()