from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .models import Park
from accounts.models import User

# Create your views here.

def index(request):
    return render(request, "main.html")

def park(request):
    park_list = Park.objects.all()
    return render(request, "park.html", {'park_list': park_list})

def booking(request, pk):
    park_detail = get_object_or_404(Park,pk=pk)
    if request.method == 'POST':        
        if request.user.is_booked == False and park_detail.can_booked:
            park_detail.seat_count -= 1
            if park_detail.seat_count == 0:
                park_detail.can_booked = False
            request.user.is_booked = True
            request.user.park = park_detail
            request.user.save()
            park_detail.save()
        else: 
            print("예약됨", request.user.is_booked)
            
        return  HttpResponseRedirect('/park')
    else:
        return render(request, 'booking.html', {'park_detail':park_detail})
    
def mybooking(request):
    user = request.user
    user_park = request.user.park
    if user_park is not None:
        park_detail = get_object_or_404(Park,pk=user_park.pk)
        if request.method == 'POST':
            if user.is_booked == True:
                user.is_booked = False
                park_detail.seat_count += 1
                if park_detail.seat_count > 0:
                    park_detail.can_booked = True
                user.park = None
                user.save()
                park_detail.save()

    return render(request, "mybooking.html", {'park_detail': user_park})

def gotopark(request):
    return HttpResponseRedirect("/park")