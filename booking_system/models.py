from django.db import models
from django.conf import settings

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    locatio = models.TextField()
    descriptiom = models.TextField()

    def __str__(self):
        return f"Room #{self.number}"    

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}, {self.room}"
    

    class Meta():
        ordering = ["start_time"]

