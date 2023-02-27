from rest_framework import viewsets
from . import loginfile
from . import loginserializers

class LoginViewset(viewsets.ModelViewSet):
    queryset = loginfile.Login.objects.all()
    serializer_class = loginserializers.LoginSerializer