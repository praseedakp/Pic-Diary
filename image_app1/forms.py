from django import forms




#regform:
class regform(forms.Form):
    fname=forms.CharField(max_length=100)
    emailone=forms.EmailField()
    userna=forms.CharField(max_length=100)
    passw=forms.CharField(max_length=100)
    cpass=forms.CharField(max_length=100)



#login :
class loginform(forms.Form):
    username=forms.CharField(max_length=100)
    passw=forms.CharField(max_length=100)


#imageform:
class imageforms(forms.Form):
    image=forms.FileField()
    imagename=forms.CharField(max_length=100)



# forms of admin page:
class adminform(forms.Form):
    adminusername=forms.CharField(max_length=50)
    adminpassw=forms.CharField(max_length=50)


#adminimageforms:
class adminimageforms(forms.Form):
    aimage=forms.FileField()
    aimagename=forms.CharField(max_length=100)


class backgroundforms(forms.Form):
    bimage=forms.FileField()
    feature=forms.CharField(max_length=100)



