from rest_framework import serializers
from api.models import *

class TournamanetMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentMatch
        fields = '__all__'