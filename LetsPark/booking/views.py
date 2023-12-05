from django.shortcuts import render
from django.http import HttpResponse
from .models import Park
# Create your views here.

def index(request):
    return render(request, "main.html")

def park(request):
    park_list = Park.objects.all()
    return render(request, "park.html", {'park_list': park_list})

def booking(request, pk):
    park_detail = Park.objects.get(pk=pk)
    return render(request, 'booking.html', {'park_detail':park_detail})