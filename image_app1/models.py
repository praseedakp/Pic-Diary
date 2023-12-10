from django.db import models

# Create your models here.
#registration:
class regmodel(models.Model):
    fname=models.CharField(max_length=100)
    emailone=models.EmailField()
    userna=models.CharField(max_length=100)
    passw=models.CharField(max_length=100)





#image upload models:user
class imagemodel(models.Model):
    image=models.FileField(upload_to='image_app1/static')
    imagename=models.CharField(max_length=100)


#admin image upload:
class adminimagemodel(models.Model):
    aimage=models.FileField(upload_to='image_app1/static')
    aimagename=models.CharField(max_length=100)


#background,wallpaper and images:
class backgroundmodel(models.Model):
    bimage=models.FileField(upload_to='image_app1/static')
    feature=models.CharField(max_length=100)

