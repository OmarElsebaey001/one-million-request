from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Asset
from .serializers import AssetSerializer

class AssetDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows a specific asset to be viewed.
    
    Retrieves a specific asset by its ID.
    URL: /api/assets/<id>/
    Method: GET
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
