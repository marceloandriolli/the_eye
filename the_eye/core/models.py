from django.db import models


class EventType(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = [['category', 'name']]


class Event(models.Model):
    type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    data = models.JSONField()


class Session(models.Model):
    session_id = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
