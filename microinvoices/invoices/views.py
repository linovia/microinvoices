from rest_framework import viewsets
from . import serializers, models


class Invoice(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.Invoice
