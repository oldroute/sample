from rest_framework.serializers import ModelSerializer
from .models import Planet


class PlanetSerializer(ModelSerializer):

    class Meta:
        model = Planet
        fields = '__all__'
