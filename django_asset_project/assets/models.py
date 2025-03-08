from django.db import models
from django.utils import timezone

class Asset(models.Model):
    """Model representing an asset in the system"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    asset_type = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    location = models.CharField(max_length=255, blank=True, null=True)
    acquisition_date = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('maintenance', 'Under Maintenance'),
            ('retired', 'Retired'),
        ],
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'
