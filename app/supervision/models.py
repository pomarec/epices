from django.db import models


class Inverter(models.Model):
    pass


class Measure(models.Model):
    inverter = models.ForeignKey(Inverter, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    energy = models.PositiveIntegerField()

    def __str__(self):
        return f"<id: {self.id}, inverter: {self.inverter.id}, datetime: {self.datetime}, energy: {self.energy}"
