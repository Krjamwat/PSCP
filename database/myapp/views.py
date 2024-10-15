# myapp/views.py
from django.shortcuts import render, redirect
from .models import Booking, Room  # Make sure Room is imported
from .forms import BookingForm
import json

def room_calendar(request):
    bookings = Booking.objects.all()

    # Create a list of events for the calendar
    events = []
    for booking in bookings:
        events.append({
            'title': booking.room.name + ' - ' + (booking.user.username if booking.user else booking.anonymous_user_name),
            'start': booking.start_time.isoformat(),
            'end': booking.end_time.isoformat(),
        })

    # Pass the events to the template
    context = {
        'events': json.dumps(events),  # Convert the events list to JSON
    }

    return render(request, 'room_calendar.html', context)

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user  # If user is logged in
            else:
                booking.anonymous_user_name = form.cleaned_data['anonymous_user_name']  # If anonymous
            booking.save()
            return redirect('room_calendar')  # Redirect to the calendar after booking
    else:
        form = BookingForm()

    return render(request, 'book_room.html', {'form': form})
