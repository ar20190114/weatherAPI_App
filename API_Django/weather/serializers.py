from rest_framework import serializers
from dataclasses import field
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        field = ['id', 'location', 'weather', 'temperature']