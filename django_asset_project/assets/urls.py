from django.urls import path
from .views import AssetDetailView

urlpatterns = [
    path('<int:pk>/', AssetDetailView.as_view(), name='asset-detail'),
]
