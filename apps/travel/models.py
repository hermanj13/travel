from __future__ import unicode_literals
from django.db import models
from datetime import date
from ..login.models import User
from django.contrib import messages

# Create your models here.
class TravelersManager(models.Manager):
    def validate(self, validate, request):
        if Trips.objects.filter(id = validate['trip']).filter(creater__id = validate['user']).exists():
            messages.error(request, 'You created this event!')
        else:
            Travelers.objects.create(booked_id = validate['user'], destination_id = validate['trip'])

class TripsManager(models.Manager):
    def validate(self, validate, request):
        today = str(date.today())
        if today < validate['start']:
            if validate['start'] < validate['end']:
                Trips.objects.create(destination = validate['destination'], description = validate['description'], start = validate['start'], end = validate['end'], creater_id = request.session['id'])
                return False
            else:
                messages.error(request, 'End Date can not be before start date!')
                return True
        else:
            messages.error(request, 'Date can not be before today!')
            return True



class Trips(models.Model):
    destination = models.CharField(max_length=60)
    description = models.CharField(max_length=90)
    start = models.DateField()
    end = models.DateField()
    creater = models.ForeignKey(User, related_name = "trips_user")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripsManager()

class Travelers(models.Model):
    booked = models.ForeignKey(User, related_name = "travelers_user")
    destination = models.ForeignKey(Trips, related_name = "travelers_trip")
    objects = TravelersManager()
