from django.urls import path
from .views import Sensors, SensorPatch, Measurements

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path("sensors/", Sensors.as_view()),
    path("sensors/<pk>/", SensorPatch.as_view()),
    path("measurements/", Measurements.as_view()),
]
