from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    """Serializer for the Asset model"""
    
    class Meta:
        model = Asset
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
