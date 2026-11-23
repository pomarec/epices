from datetime import datetime

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.supervision.ingesters import MeasureIngester
from app.supervision.serialiazers import MeasureSerializer

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

    measures = Measure.objects.filter(datetime__date=date)
    context["measures"] = measures
    energy_sum = sum(m.energy for m in measures)
    context["energy_sum"] = energy_sum

    return render(request, "index.html", context)


def upload(request):
    """
    Upload measures in a file.
    """

    class UploadMeasureFileForm(forms.Form):
        file = forms.FileField()

    if request.method == "POST":
        form = UploadMeasureFileForm(request.POST, request.FILES)
        if form.is_valid():
            measures = MeasureSerializer().fromFile(request.FILES["file"])
            MeasureIngester().ingest(measures)
            return HttpResponseRedirect("/")
    else:
        form = UploadMeasureFileForm()
    return render(request, "upload.html", {"form": form})
