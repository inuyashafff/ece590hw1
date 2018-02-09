from django.shortcuts import render,redirect
from rsvp.forms import RegistrationForm,EditProfileForm,CreateEventForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from rsvp import models
from django.contrib.auth.decorators import login_required

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
            return render(request, 'rsvp/reg_form.html',{})
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
            form.save()
            return redirect('http://vcm-2971.vm.duke.edu:8080/rsvp/profile')
        else:
            form= CreateEventForm()
            args= {'form':form}
            return render(request, 'rsvp/create_event.html',args)
    else:
        form= CreateEventForm()
        args= {'form':form}
        return render(request, 'rsvp/create_event.html',args)

    
# Create your views here.
