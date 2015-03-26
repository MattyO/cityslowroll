from django.db import models

class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    place = models.CharField(max_length=150)


class SlowRoll(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    from_address=models.CharField(max_length=100)
    event_time=models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    location= models.ForeignKey(Location, blank=True, null=True)

    def __str__(self):
        return self.title

