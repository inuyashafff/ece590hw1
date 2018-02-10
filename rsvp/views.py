from django.shortcuts import render,redirect
from rsvp.forms import RegistrationForm,EditProfileForm,CreateEventForm,InviteGuest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from rsvp import models
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

def home(request):
    return render(request, 'rsvp/home.html')
def register(request):
    if request.method=='POST':
        form= RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://vcm-2971.vm.duke.edu:8080/rsvp/login')
            #return render(request, 'rsvp/home.html',{})
            #HttpResponseRedirect('/rsvp/')
        else:
            form= RegistrationForm()
            args = {'form':form}
            return render(request, 'rsvp/reg_form.html',args)
    else:
        form= RegistrationForm()
        args = {'form':form}
        return render(request, 'rsvp/reg_form.html',args)
    
#@login_required
def profile(request):
    args={'user':request.user}
    return render(request,'rsvp/profile.html',args)
#@login_required
def edit_profile(request):
    if request.method=='POST':
        form= EditProfileForm(data=request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('http://vcm-2971.vm.duke.edu:8080/rsvp/profile')
    else:
        form= EditProfileForm(instance = request.user)
        args= {'form':form}
        return render(request, 'rsvp/edit_profile.html',args)
#@login_required
def change_password(request):
    if request.method=='POST':
        form= PasswordChangeForm(data=request.POST,user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('http://vcm-2971.vm.duke.edu:8080/rsvp/profile')
        else:
            return redirect('http://vcm-2971.vm.duke.edu:8080/rsvp/change-password')
    else:
        form= PasswordChangeForm(user = request.user)
        args= {'form':form}
        return render(request, 'rsvp/change_password.html',args)
#@login_required
def create_event(request):
    if request.method=='POST':
        form = CreateEventForm(data=request.POST)
        #mei you yan zheng valid
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.user_position = 'Owner'
            form.save()
            return redirect('http://vcm-2971.vm.duke.edu:8080/rsvp/profile/create-event/invite-guest')
            #return render(request, 'rsvp/invite_guest.html',{})
        else:
            form= CreateEventForm()
            args= {'form':form}
            return render(request, 'rsvp/create_event.html',args)
    else:
        form= CreateEventForm()
        args= {'form':form}
        return render(request, 'rsvp/create_event.html',args)

def invite_guest(request):
    #template_name ='rsvp/invite_guest.html'

    if request.method!='POST':
        form = InviteGuest()
        eventName= models.Event.objects.all().order_by('-created')[1].name
        #event can not have the same name
        posts = models.Event.objects.filter(name=eventName,user_position='Guest').order_by('-created')
        args ={'form':form, 'posts':posts,}
        return render(request,'rsvp/invite_guest.html',args)

    else:
        form = InviteGuest(data = request.POST)
        if form.is_valid():
            #form = form.save(commit=False)
            #if models.Event.objects.filter(user=request.POST)!=[]:
                #redirect('http://vcm-2971.vm.duke.edu:8080/rsvp/profile/create-event/invite-guest')
            form = form.save(commit=False)
            form.name = models.Event.objects.all().order_by('-created')[1].name
            form.user_position='Guest'
            form.save()
            #have not saved in database, need the event name to save
            #text = form.cleaned_data['user']
            form = InviteGuest()
        eventName= models.Event.objects.all().order_by('-created')[1].name
        posts = models.Event.objects.filter(name=eventName,user_position='Guest').order_by('-created')
        args = {'form':form,'posts':posts,}
        return render(request,'rsvp/invite_guest.html',args)
    
# Create your views here.
