from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import MeasureSerializer
from .models import Measure


class SnippetViewSet(viewsets.ModelViewSet):
    """
    viewset to provide `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Measure model
    """
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

