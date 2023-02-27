from rest_framework import viewsets
from . import booklabmodels
from . import booklabserializers

class BookLabViewset(viewsets.ModelViewSet):
    queryset = booklabmodels.BookLab.objects.all()
    serializer_class = booklabserializers.BookLabSerializer