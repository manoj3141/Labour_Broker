from django.urls import path
from .views import *
urlpatterns = [
    path('home',home,name='home'),
    path('',ulogin,name='login'),
    path('signup/',usignup,name='signup'),
    path('logout/',ulogout,name='logout'),
    path('choices/',showchoice,name='showchoice'),
    path('choice/',choosechoice,name='choice'),
    path('labourform/',labour_form,name='labourform'),
    path('ai/',ai,name='ai'),
    path('profile/',profile,name='profile'),
    path('showlabour/',showlabour,name='searchlabour'),
    path('showprofile/',showprofile,name='showprofile')
]