from django import forms
from django.contrib.auth.models import User
from signupform.models import Userinfo,Contactinfo,UserPostedImages
import re

# class UserForm(forms.Form):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username','password','email']
        
# class SignupForm(forms.Form):  
#     class Meta:
#         model = Userinfo
#         fields = ['mobilenumber','address','dob']

class SignupForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    MobileNumber = forms.IntegerField()
    Address = forms.CharField()
    DateOfBirth = forms.DateField()

    def clean_name(self):
        input_name = self.cleaned_data['name']
        user_name = User.objects.filter(username=input_name)
        print(user_name)
        if len(user_name)>0:
            raise forms.ValidationError("Username is already exits")
        return input_name
    
    def clean_email(self):
        input_email = self.cleaned_data['email']
        user_email = User.objects.filter(email=input_email)
        print(user_email)
        if len(user_email)>0:
            raise forms.ValidationError("Email is already exits")
        return input_email

    def clean_MobileNumber(self):
        input_MobileNumber = self.cleaned_data['MobileNumber']
        user_MobileNumber = Userinfo.objects.filter(mobilenumber=input_MobileNumber)
        print(user_MobileNumber)
        if len(user_MobileNumber)>0:
            raise forms.ValidationError("Mobile Number is already exits")
        return input_MobileNumber

        
class ContactForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) == 0:
            raise forms.ValidationError("Please enter your name")
        input_name = re.match('[a-zA-Z]',username)
        if input_name ==None:
            raise forms.ValidationError("Please provide valid username")

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) == 0:
            raise forms.ValidationError("Please enter your email id")

        input_email = re.match('\w+@gmail.com$',email)
        if input_email ==None:
            raise forms.ValidationError("Only gmail email id are except here..or please Provide valid email id")

        return email
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) == 0:
            raise forms.ValidationError("Please enter your name")
       
        return message

    # def clean(self):
    #     total_cleaned_data =super().clean()
    #     print(total_cleaned_data)
    #     name = total_cleaned_data['username']
    #     email = total_cleaned_data['email']
    #     message = total_cleaned_data['message']

    #     if len(name) == 0:
    #         raise forms.ValidationError("Please enter your name")

    #     input_name = re.match('\w+',name)
    #     if input_name ==None:
    #         raise forms.ValidationError("Please provide valid username")

       
    #     if len(email) == 0:
    #         raise forms.ValidationError("Please enter your Email")
        
    #     input_email = re.match('\w+@gmail.com$',email)
    #     if input_email == None:
    #         raise forms.ValidationError("Only gmail email id are except here..or please Provide valid email id")

    #     if len(message) == 0:
    #         raise forms.ValidationError("Please Enter your body")

class UserUploadedPostForm(forms.Form):
    class Meta:
        model = UserPostedImages
        fields = ['post_image',]

class EditForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    MobileNumber = forms.IntegerField()
    Address = forms.CharField()
    DateOfBirth = forms.DateField()
    
        































        


