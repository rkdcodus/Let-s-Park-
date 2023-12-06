from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .models import Park
# Create your views here.

def index(request):
    return render(request, "main.html")

def park(request):
    park_list = Park.objects.all()
    return render(request, "park.html", {'park_list': park_list})

def booking(request, pk):
    park_detail = get_object_or_404(Park,pk=pk)
    if request.method == 'POST':
        park_detail.seat_count -= 1
        park_detail.save()
        return  HttpResponseRedirect('/booking/park')
    else:
        return render(request, 'booking.html', {'park_detail':park_detail})