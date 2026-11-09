from django.contrib import admin

from app.supervision.models import Inverter, Measure

admin.site.register(Inverter)
admin.site.register(Measure)
