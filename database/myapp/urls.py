# myapp/urls.py
from django.urls import path
from .views import room_calendar,book_room

urlpatterns = [
    path('', room_calendar, name='room_calendar'),  # You can leave this as is or specify another view
    path('book/', book_room, name='book_room'),
]
