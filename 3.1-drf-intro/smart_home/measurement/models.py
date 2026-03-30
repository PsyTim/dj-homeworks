from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True)
    image = models.ImageField(null=True, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        # to_field="measurement",
        related_name="measurements",
    )
    temperature = models.FloatField()
    # created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
