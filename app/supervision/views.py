from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import Measure


def index(request):
    """
    Consult measures of a given date.
    """
    context = {}

    date_param = request.GET.get("date")
    date = (
        datetime.strptime(date_param, "%Y-%m-%d")
        if date_param is not None
        else datetime.today()
    )
    context["date"] = date

    if date_param:
        measures = Measure.objects.filter(datetime__date=date.date())
        context["measures"] = measures
        energy_sum = sum(m.energy for m in measures)
        context["energy_sum"] = energy_sum

    return render(request, "index.html", context)
