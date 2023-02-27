from rest_framework import viewsets
from . import labimagemodels
from . import labimageserializer

class LabImageViewset(viewsets.ModelViewSet):
    queryset = labimagemodels.LabImage.objects.all()
    serializer_class = labimageserializer.LabImageSerializer

