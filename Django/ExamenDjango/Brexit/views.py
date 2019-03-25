from django.shortcuts import render
import datetime

from django.utils import timezone

from .models import Brexit
import string


def index(request):
    dateNow = timezone.now()
    dateBrexit = datetime.datetime(2019, 3, 29, 12)
    timeTillBrexit = dateBrexit - dateNow

    return render(request, 'Brexit/index.html', {'brexit_timeTillEnd': timeTillBrexit})
