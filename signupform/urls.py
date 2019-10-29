from django.conf.urls import url
from signupform.views import *



urlpatterns = [
    url(r'^signupform/', signupform,name='signupform'),
    url(r'^loginform/',loginform,name='loginform'),
    url(r'^logout/',user_logout,name='logout'),
    url(r'^postuploaded/',user_image_posted,name='postuploaded')   
]
