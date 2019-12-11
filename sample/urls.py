from django.contrib import admin
from django.urls import path
from sample.models import Planet
from .serializers import PlanetSerializer


from rest_framework.generics import ListAPIView


admin.site.site_header = 'Солнечная система'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', ListAPIView.as_view(
        queryset=Planet.objects.all(),
        serializer_class=PlanetSerializer)
    )
]
