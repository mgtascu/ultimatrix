from rest_framework import viewsets
from .models import ItemType, AcqItem
from .serializers import ItemTypeSerializer, AcqItemSerializer


class ItemTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer


class AcqItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AcqItem.objects.all()
    serializer_class = AcqItemSerializer
