from rest_framework import viewsets
from . import reviewmodels
from . import reviewserializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = reviewmodels.Review.objects.all()
    serializer_class = reviewserializer.ReviewSerializer