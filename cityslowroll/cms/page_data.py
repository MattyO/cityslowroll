from rolls.models import SlowRoll
from datetime import datetime
#def index():
#    all_rides = SlowRoll.objects.filter(event_time__gte=datetime.now()).order_by('event_time')
#    next_ride = all_rides[0]
#    return {'slow_rolls' : all_rides, 'next_ride': next_ride}

def rolls():
    return  {'slowrolls': SlowRoll.objects.order_by('event_time') }
