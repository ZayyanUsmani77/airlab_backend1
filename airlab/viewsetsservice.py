from rest_framework import viewsets
from . import servicemodels
from . import serviceserializer

class ServiceViewset(viewsets.ModelViewSet):
    queryset = servicemodels.Service.objects.all()
    serializer_class = serviceserializer.ServiceSerializer