from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Userinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobilenumber = models.IntegerField(null=True,blank=True)
    address = models.CharField(max_length=256,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.user.username}"

# @receiver(post_save,sender=User,weak=False)
# def userinfo_create(sender,instance,created,**kwargs):
#     if created:
#         userinfo=Userinfo(user=instance)
#         userinfo.save()u1.save
    
class Contactinfo(models.Model):
    name= models.CharField(max_length=60)
    email = models.EmailField()
    message = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"

class UserPostedImages(models.Model):
    username = models.CharField(max_length=60)
    post_image = models.ImageField(upload_to='',max_length=255)
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"
    



