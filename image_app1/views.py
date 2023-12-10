from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import os

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout




# Create your views here.

#registation:
def regview(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            k=a.cleaned_data['fname']
            l=a.cleaned_data['emailone']
            m=a.cleaned_data['userna']
            n=a.cleaned_data['passw']
            o=a.cleaned_data['cpass']
            if n==o:
                b=regmodel(fname=k,emailone=l,userna=m,passw=n)
                b.save()
                return redirect(loginview)
            else:
                return HttpResponse("password doesnot match.....")
        else:
            return HttpResponse("registration failed.....")
    return render(request,'registration.html')


#login:
def loginview(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            m=a.cleaned_data['username']
            n=a.cleaned_data['passw']
            b=regmodel.objects.all()
            for i in b:
                if i.userna==m and i.passw==n:
                    request.session['id']=i.id
                    return redirect(profileview)
            else:
                return HttpResponse("login filed")
    return render(request,'login.html')


#profilepage:
def profileview(request):
    id1=request.session['id']
    a=regmodel.objects.get(id=id1)
    return render(request,'userprofile.html',{'a':a})


#edit the profile page:
def editprofile(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.emailone=request.POST.get('emailone')
        a.userna=request.POST.get('userna')
        a.save()
        return redirect(profileview)
    return render(request,'editprofile.html',{'a':a})








#image upload
def firstview(request):
    if request.method=='POST':
        a=imageforms(request.POST,request.FILES)
        if a.is_valid():
            im=a.cleaned_data['image']
            na=a.cleaned_data['imagename']
            b=imagemodel(image=im,imagename=na)
            b.save()
            return redirect(dispimage)
        else:
            return HttpResponse("upload failed")

    return render(request,'imageupload.html')


#display the images:
def dispimage(request):
    # id3=request.session['id']
    a=imagemodel.objects.all()
    id2=[]
    k=[]
    m=[]
    for i in a:
        id1=i.id
        id2.append(id1)
        n=str(i.image).split('/')[-1]
        k.append(n)
        o=i.imagename
        m.append(o)
    pair=zip(id2,k,m)
    return render(request,'imageupload.html',{'k':pair})


#delete the image:
def imagedelete(request,id):
    a=imagemodel.objects.get(id=id)
    os.remove(str(a.image))
    a.delete()
    return redirect(dispimage)



#image edit:
def editimage(request,id):
    a=imagemodel.objects.get(id=id)
    img=str(a.image).split('/')[-1]
    if request.method=='POST':
        a.imagename=request.POST.get('imagename')
        if len(request.FILES)!=0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.save()
        return redirect(dispimage)
    return render(request,'imageedit.html',{'a':a,'img':img})


#index page:
def indexone(request):
    return render(request,'index.html')


#about:
def aboutpage(request):
    return render(request,'about.html')

#contact
def contactpage(request):
    return render(request,'contact.html')

#photodetails
def photodetails(request):
    return render(request,'photo-detail.html')

#video details
def videodetails(request):
    return render(request,'video-detail.html')

#videos
def videoone(request):
    return render(request,'videos.html')


#admin login code:
def adminlogin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['adminusername']
            password=a.cleaned_data['adminpassw']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return redirect(adminprofile)

            else:
                return HttpResponse("Login failed")

    return render(request,'adminlogin.html')


#admin profilepage:
def adminprofile(request):
    return render(request,'adminprofilepage.html')

#admin image upload:
def adminimupload(request):
    if request.method=='POST':
        a=adminimageforms(request.POST,request.FILES)
        if a.is_valid():
            im=a.cleaned_data['aimage']
            na=a.cleaned_data['aimagename']
            b=adminimagemodel(aimage=im,aimagename=na)
            b.save()
            return redirect(admindispimage)
        else:
            return HttpResponse("upload failed")

    return render(request,'adminimageup.html')


#display the image:
def admindispimage(request):
    a=adminimagemodel.objects.all()
    id2=[]
    k=[]
    m=[]
    for i in a:
        id1=i.id
        id2.append(id1)
        n=str(i.aimage).split('/')[-1]
        k.append(n)
        o=i.aimagename
        m.append(o)
    pair=zip(id2,k,m)
    return render(request,'adminimagedisplay.html',{'d':pair})


#display the image for user:
def userdispimage(request):
    a=adminimagemodel.objects.all()
    id2=[]
    k=[]
    m=[]
    for i in a:
        id1=i.id
        id2.append(id1)
        n=str(i.aimage).split('/')[-1]
        k.append(n)
        o=i.aimagename
        m.append(o)
    pair=zip(id2,k,m)
    return render(request,'imagedisplayuser.html',{'s':pair})


#image edit:
def admineditimage(request,id):
    a=adminimagemodel.objects.get(id=id)
    img=str(a.aimage).split('/')[-1]
    if request.method=='POST':
        a.aimagename=request.POST.get('aimagename')
        if len(request.FILES)!=0:
            if len(a.aimage)>0:
                os.remove(a.aimage.path)
            a.aimage=request.FILES['aimage']
        a.save()
        return redirect(admindispimage)
    return render(request,'adminimageedit.html',{'a':a,'img':img})



#delete the image admin:
def adminimagedelete(request,id):
    a=adminimagemodel.objects.get(id=id)
    os.remove(str(a.aimage))
    a.delete()
    return redirect(admindispimage)



#single display the card for customers
def singledisplay(request,id):
    a=adminimagemodel.objects.get(id=id)
    im=str(a.aimage).split('/')[-1]
    return render(request,'singleviewpage.html',{'a':a,'im':im})




# logout:after login the page want to logout use this function
# def logout_view(request):
#     logout(request)
#     return redirect(loginview)


#background,wallpaper and images more:
#image upload
def backgroundimages(request):
    if request.method=='POST':
        a=backgroundforms(request.POST,request.FILES)
        if a.is_valid():
            im=a.cleaned_data['bimage']
            na=a.cleaned_data['feature']
            b= backgroundmodel(bimage=im,feature=na)
            b.save()
            return redirect(backgroundimagedisp)
        else:
            return HttpResponse("image upload failed")

    return render(request,'favouriteadd.html')


#display the images:
def backgroundimagedisp(request):
    a = backgroundmodel.objects.all()
    id2 = []
    k = []
    m = []
    for i in a:
        id1 = i.id
        id2.append(id1)
        n = str(i.bimage).split('/')[-1]
        k.append(n)
        o = i.feature
        m.append(o)
    pair = zip(id2, k, m)
    return render(request, 'adminfavdisplay.html', {'d': pair})


#image edit:
def admineditbimage(request,id):
    a=backgroundmodel.objects.get(id=id)
    img=str(a.bimage).split('/')[-1]
    if request.method=='POST':
        a.feature=request.POST.get('feature')
        if len(request.FILES)!=0:
            if len(a.bimage)>0:
                os.remove(a.bimage.path)
            a.bimage=request.FILES['bimage']
        a.save()
        return redirect(backgroundimagedisp)
    return render(request,'adminbackimageedit.html',{'a':a,'img':img})



#delete the image admin:
def adminbimagedelete(request,id):
    a=backgroundmodel.objects.get(id=id)
    os.remove(str(a.bimage))
    a.delete()
    return redirect(backgroundimagedisp)




#display the all images for user:
def userbackgrounddisp(request):
    a=backgroundmodel.objects.all()
    id2=[]
    k=[]
    m=[]
    for i in a:
        id1=i.id
        id2.append(id1)
        n=str(i.bimage).split('/')[-1]
        k.append(n)
        o=i.feature
        m.append(o)
    pair=zip(id2,k,m)
    return render(request,'backimagedisplayuser.html',{'s':pair})


#single all image display:
def singledisplyall(request,id):
    a=backgroundmodel.objects.get(id=id)
    im=str(a.bimage).split('/')[-1]
    return render(request,'singleviewallimages.html',{'a':a,'im':im})


#all display for user:
def allbackgrounddisp(request):
    a=backgroundmodel.objects.all()
    id2=[]
    k=[]
    m=[]
    for i in a:
        id1=i.id
        id2.append(id1)
        n=str(i.bimage).split('/')[-1]
        k.append(n)
        o=i.feature
        m.append(o)
    pair=zip(id2,k,m)
    return render(request,'bcwdisplayonly.html',{'s':pair})


#terms:
def terms(request):
    return render(request,'termsandcondition.html')