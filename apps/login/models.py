from __future__ import unicode_literals
import re, bcrypt
from django.db import models
from django.contrib import messages

# Create your models here.
class UserManager(models.Manager):
    def regvalidate(selt, validate, request):
        if User.objects.filter(username = validate['username']).exists():
            messages.error(request, 'Username Already Registered', extra_tags='register')
            return True
        else:
            if len(validate['name']) >= 3:
                if len(validate['username']) >= 3:
                    if len(validate['password']) >= 8:
                        if validate['password'] == validate['confirm']:
                            password = bcrypt.hashpw(str(validate['password']), bcrypt.gensalt())
                            User.objects.create(name = validate['name'], username = validate['username'], password = password)
                            request.session['id'] = User.objects.only('id').get(username = validate['username']).id
                            request.session['name'] = validate['name']
                            return False
                        else:
                            print '1'
                            messages.error(request, 'Passwords do not match.', extra_tags='register')
                            return True
                    else:
                        print '2'
                        messages.error(request, 'Invalid Password, must be no fewer then 8 characters.', extra_tags='register')
                        return True
                else:
                    print '3'
                    messages.error(request, 'Invalid Username, must be no fewer then 2 characters.', extra_tags='register')
                    if not len(validate['password']) >= 8:
                        messages.error(request, 'Invalid Password, must be no fewer then 8 characters.', extra_tags='register')
                    elif validate['password'] != validate['confirm']:
                        messages.error(request, 'Passwords do not match.', extra_tags='register')
                    return True
            else:
                messages.error(request, 'Invalid Name, must be no fewer then 3 characters.', extra_tags='register')
                if not len(validate['username']) >= 2:
                    messages.error(request, 'Invalid Username, must be no fewer then 3 characters.', extra_tags='register')
                if not len(validate['password']) >= 8:
                    messages.error(request, 'Invalid Password, must be no fewer then 8 characters.', extra_tags='register')
                elif validate['password'] != validate['confirm']:
                    messages.error(request, 'Passwords do not match.', extra_tags='register')
                return True
    def loginvalidate(self,validate,request):
        if User.objects.filter(username = validate['username']).exists():
            hashed = str(User.objects.only('password').get(username = validate['username']).password)
            if hashed == bcrypt.hashpw(str(validate['password']), hashed):
                request.session['id'] = User.objects.only('id').get(username = validate['username']).id
                request.session['name'] = User.objects.only('name').get(username = validate['username']).name
                return False
            else:
                messages.warning(request, 'Passwords Do Not Match, Please Try Again.', extra_tags='login')
                return True
        else:
            messages.warning(request, 'Username Not Registed, Please Sign Up!', extra_tags='login')
            return True

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
