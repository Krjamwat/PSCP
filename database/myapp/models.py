# myapp/models.py
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL)
    anonymous_user_name = models.CharField(max_length=255, null=True, blank=True)  # For anonymous users
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.room.name} booked by {self.user or self.anonymous_user_name}'
