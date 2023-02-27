from rest_framework import viewsets
from . import labmodels
from . import labserializers

class LabViewset(viewsets.ModelViewSet):
    queryset = labmodels.Lab.objects.all()
    serializer_class = labserializers.LabSerializer


#list() , retrive(), create() , update(), destroy()