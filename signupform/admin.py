from django.contrib import admin
from signupform.models import Userinfo,Contactinfo

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    list_display = ['id','mobilenumber']

admin.site.register(Userinfo,SignupAdmin)

class ContactinfoAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']

admin.site.register(Contactinfo,ContactinfoAdmin)


