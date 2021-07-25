from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
import datetime

# Create your views here.

def index(request):
    context = {
        "date": strftime("%Y-%m-%d", gmtime()),
        "time": strftime("%H:%M %p", gmtime()),
        "datetime":datetime.datetime.now(),
    }
    return render(request,"index.html",context)
