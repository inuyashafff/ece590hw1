from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    description= models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    website=models.URLField(default='')
    phone = models.IntegerField(default=0)

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile= UserProfile.objects.create(user=kwargs['instance'])
        #user_profile= User.objects.create(user=kwargs['instance'])  
    
post_save.connect(create_profile,sender=User)

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    user_position = models.CharField(max_length=100,default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
"""def create_event(sender,**kwargs):
    if kwargs['created']:
        event = Event.objects.create(user=kwargs['user'])

post_save.connect(create_event,sender=User)
"""
# Create your models here.
