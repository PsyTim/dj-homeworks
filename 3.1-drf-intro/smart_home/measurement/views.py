# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
)
from .models import Sensor

from .serializers import (
    SensorsSerializer,
    MeasurementSerializer,
    SensorDetailSerializer,
)


class Sensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorPatch(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    # allowed_methods = ["GET", "PATCH"]


class Measurements(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
