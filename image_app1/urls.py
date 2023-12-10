from django.urls import path
from .views import *

urlpatterns=[
    path('firstview/',firstview),
    path('dispimage/',dispimage),
    path('imagedelete/<int:id>',imagedelete),
    path('regview/',regview),
    path('loginview/',loginview),
    path('profileview/',profileview),
    path('editprofile/<int:id>',editprofile),
    path('imageedit/<int:id>',editimage),
    path('indexone/',indexone),
    path('adminlogin/',adminlogin),
    path('adminprofile/',adminprofile),
    path('aboutpage/',aboutpage),
    path('contactpage/',contactpage),
    path('photodetails/',photodetails),
    path('videodetails/',videodetails),
    path('videoone/',videoone),
    path('adminimupload/',adminimupload),
    path('admindispimage/',admindispimage),
    path('userdispimage/',userdispimage),
    path('admineditimage/<int:id>',admineditimage),
    path('adminimagedelete/<int:id>',adminimagedelete),
    path('singlediaplyone/<int:id>',singledisplay),
    path('backgroundimages/',backgroundimages),
    path('backgroundimagedisp/',backgroundimagedisp),
    path('admineditbimage/<int:id>',admineditbimage),
    path('adminbimagedelete/<int:id>',adminbimagedelete),
    path('userbackgrounddisp/',userbackgrounddisp),
    path('singledisplyall/<int:id>',singledisplyall),
    path('allbackgrounddisp/',allbackgrounddisp),
    path('terms/',terms)



]