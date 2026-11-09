from django.db import models


class Inverter(models.Model):
    pass


class Measure(models.Model):
    inverter = models.ForeignKey(Inverter, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    energy = models.PositiveIntegerField()
