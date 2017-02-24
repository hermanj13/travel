from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from datetime import date
from .models import Trips, Travelers
from ..login.models import User
# Create your views here.

def index(request):
    if not 'id' in request.session:
        return redirect(reverse('login:index'))
    else:
        context = {
            'trips_made' : Trips.objects.filter(creater__id = request.session['id']),
            'trips_join' : Trips.objects.filter(travelers_trip__booked__id = request.session['id']),
            'others' : Trips.objects.exclude(creater__id = request.session['id'])&Trips.objects.exclude(travelers_trip__booked__id = request.session['id'])
        }
        return render(request, 'travel/index.html', context)

def join(request, id):
    if not 'id' in request.session:
        return redirect(reverse('login:index'))
    else:
        validate = {
            'user' : request.session['id'],
            'trip' : id
        }
        Travelers.objects.validate(validate, request)
        return redirect(reverse('travel:index'))

def add(request):
    if not 'id' in request.session:
        return redirect(reverse('login:index'))
    else:
        return render(request, 'travel/add.html')

def new(request):
    if not 'id' in request.session:
        return redirect(reverse('login:index'))
    else:
        if request.method == 'POST':
            flag = False
            validate = {
                'destination' : request.POST['dest'],
                'description' : request.POST['desc'],
                'start' : request.POST['start'],
                'end' : request.POST['end']
            }
            flag = Trips.objects.validate(validate,request)
            if flag == True:
                return redirect(reverse('travel:add'))
            if flag == False:
                return redirect(reverse('travel:index'))
        else:
            return redirect(reverse('travel:index'))

def dest(request,id):
    if not 'id' in request.session:
        return redirect(reverse('login:index'))
    else:
        context = {
            'trips' : Trips.objects.filter(id = id),
            'other' : Travelers.objects.filter(destination = id)
        }
        return render(request, 'travel/dest.html', context)
