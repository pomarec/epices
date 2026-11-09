from django.http import HttpResponse


def index(request):
    return HttpResponse("""See measures and upload new data.""")
