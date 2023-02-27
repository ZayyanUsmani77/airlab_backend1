from rest_framework import viewsets
from . import contactlabmodels
from . import contactlabserializer

class ContactLabViewset(viewsets.ModelViewSet):
    queryset = contactlabmodels.ContactLab.objects.all()
    serializer_class = contactlabserializer.ContactLabSerializer

