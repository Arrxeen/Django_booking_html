from django.urls import path
from booking_system import views

urlpatterns = [
    path('room-list/', views.room_list, name="room-list"),
    path("book-room/", views.book_room, name="book-room"),
    path('boking-details/<int:pk>', views.bookin_details, name='booking-detail'),
    path('user_booking/', views.user_booking, name="user_booking")
]
