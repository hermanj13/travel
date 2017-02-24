from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User

# Create your views here.

def index(request):
    if 'id' in request.session:
        return redirect(reverse('travel:index'))
    else:
        return render(request, 'login/index.html')

def register(request):
    if 'id' in request.session:
        return redirect(reverse('travel:index'))
    else:
        if request.method == 'POST':
            flag = False
            validate = {
                'name':request.POST['name'],
                'username':request.POST['username'],
                'password':request.POST['password'],
                'confirm':request.POST['pwconf']
            }
            flag = User.objects.regvalidate(validate,request)
            if flag == True:
                return redirect(reverse('login:index'))
            if flag == False:
                return redirect(reverse('travel:index'))
        else:
            return redirect(reverse('login:index'))

def login(request):
    if 'id' in request.session:
        return redirect(reverse('travel:index'))
    else:
        if request.method == 'POST':
            flag = False
            validate = {
                'username':request.POST['username'],
                'password':request.POST['password']
            }
            flag = User.objects.loginvalidate(validate,request)
            if flag == True:
                return redirect(reverse('login:index'))
            if flag == False:
                return redirect(reverse('travel:index'))
        else:
            return redirect(reverse('login:index'))

def logout(request):
    request.session.flush()
    return redirect(reverse('login:index'))
