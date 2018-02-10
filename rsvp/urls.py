from django.urls import path
from . import views
from django.contrib.auth.views import login,logout
#app_name = 'polls'

urlpatterns = [
    path('',views.home),
    path('login/', login, {'template_name':'rsvp/login.html'}),
    path('logout/', logout, {'template_name':'rsvp/logout.html'}),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('change-password/',views.change_password,name='change_password'),
    path('profile/create-event/',views.create_event,name='create_event'),
    path('profile/create-event/invite-guest/',views.invite_guest,name='invite_guest'),
]
