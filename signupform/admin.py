from django.contrib import admin
from signupform.models import Userinfo,Contactinfo,UserPostedImages,Likecount

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    list_display = ['id','mobilenumber']

admin.site.register(Userinfo,SignupAdmin)

class ContactinfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']

admin.site.register(Contactinfo,ContactinfoAdmin)

class Useruploadedpostadmin(admin.ModelAdmin):
    list_display = ['id','username','post_image','post_date','like']

admin.site.register(UserPostedImages,Useruploadedpostadmin)

class LikecountAdmin(admin.ModelAdmin):
    list_display = ['id','username','post_image_id','like_count']

admin.site.register(Likecount,LikecountAdmin)


