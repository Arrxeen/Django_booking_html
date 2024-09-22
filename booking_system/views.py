from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Booking, Room
from . import models
from django.contrib.auth.models import User

def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, "booking/room_list.html", context)

# def user_list(request):
#     user = User.objects.all()
#     context = {
#         "users": user
#     }
#     return render(request, "booking/user_list.html", context)

def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room=number")
        start_time = request.POST.get("start=time")
        end_time = request.POST.get("end=time")
        try:
            room = Room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse("wrong number", status=400)
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            start_time=start_time,
            end_time=end_time
        )
        return redirect("booking-detail", pk=booking.id)
    else:
        return render(request, template_name="booking/booking_form.html")
    
def bookin_details(request, pk):
    book = Booking.objects.get(id=pk)
    context = {
        "books": book
        }
    return render(request, "booking/booking_detail.html",context=context)

def user_booking(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    context = {
        'bookings': bookings
    }
    return render(request,"booking/bookings_user.html",context)