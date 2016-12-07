# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
import datetime

from django.utils.timezone import now


def home(request):
    today = datetime.date.today()
    return render_to_response("backend/index.html", {'today': today, 'now': now()})


def home_files(request, filename):
    return render_to_response(filename, content_type="text/plain")
