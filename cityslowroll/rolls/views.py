from django.shortcuts import render
from rolls.models import SlowRoll
from cms.helpers import nav

def rolls(request):
    rolls = SlowRoll.objects.all()
    return render(request, 'rolls/index.html', {'rolls': rolls, 'nav':nav})

def event(request, event_id):
    event = SlowRoll.objects.get(pk=event_id)
    return render(request, 'rolls/event.html', {"event": event, 'nav':nav})
