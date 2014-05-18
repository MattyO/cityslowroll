from django.db import models

class SlowRoll(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    from_address=models.CharField(max_length=100)
    to_address=models.CharField(max_length=100, null=True, blank=True)
    event_time=models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
