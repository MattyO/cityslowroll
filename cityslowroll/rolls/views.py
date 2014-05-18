from django.shortcuts import render
from rolls.models import SlowRoll

def event(request, event_id):
    event = SlowRoll.objects.get(pk=event_id)
    return render(request, 'rolls/event.html', {"event": event})
