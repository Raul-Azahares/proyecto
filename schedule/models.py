import datetime

from django.db import models
from django.urls import reverse

from authentication.models import UserProfile
from schedule.choices import STATE_DATES


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    date_start_time = models.DateField()
    time_start_time = models.TimeField()
    end_time = models.DateTimeField()
    date_end_time = models.DateField()
    time_end_time = models.TimeField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.start_time = datetime.datetime.combine(self.date_start_time,self.time_start_time)
        self.end_time = datetime.datetime.combine(self.date_end_time,self.time_end_time)
        super(Event,self).save(*args, **kwargs)

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class Dates(models.Model):
    requester = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="requester")
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    state = models.CharField(max_length=10,choices=STATE_DATES,default="Pendiente")
    date_start_time = models.DateField()
    time_start_time = models.TimeField()
    date_end_time = models.DateField()
    time_end_time = models.TimeField()
    agent = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name="agent")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.start_time = datetime.datetime.combine(self.date_start_time,self.time_start_time)
        self.end_time = datetime.datetime.combine(self.date_end_time,self.time_end_time)
        super(Dates,self).save(*args, **kwargs)


REQUESTED_GROUP_NAME = 'Solicitado'
APPLICANT_GROUP_NAME = 'Solicitante'

class Configuration(models.Model):
        parameter = models.CharField(max_length=50)
        value = models.CharField(max_length=100)










