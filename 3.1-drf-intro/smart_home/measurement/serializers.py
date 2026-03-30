from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from .models import Measurement, Sensor


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "name", "description", "image"]


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["temperature", "created_at", "sensor"]


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ["id", "name", "description", "image", "measurements"]
