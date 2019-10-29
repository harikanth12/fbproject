from django.shortcuts import render,redirect
from signupform.forms import SignupForm,ContactForm,UserUploadedPostForm
from signupform.models import Userinfo,Contactinfo
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signupform(request):
    form = SignupForm()
    if request.method == "POST":
        # user = UserForm(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'])
            MobileNumber = form.cleaned_data['MobileNumber']
            Address = form.cleaned_data['Address']
            DateOfBirth =form.cleaned_data['DateOfBirth']
            user_data = User(username=name,email=email,password=password)
            user_data.save()

            ## for one to one field ..for reference we have to pass the User Instance thats means user_data
            user_info = Userinfo(user = user_data,mobilenumber=MobileNumber,address=Address,dob=DateOfBirth)
            user_info.save()
            
    return render(request,'signupform/signupform.html',{'form':form})

def home(request):
    return render(request,'home.html')

def loginform(request):
    if request.method == "POST":
        context = {}
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=user_name,password=password)
        if user:
            login(request,user)
            return redirect(home)
        else:
            context['error'] = "Please valid credentinals !!!"
            return render(request,'signupform/loginform.html',context)
    return render(request,'signupform/loginform.html')

def user_logout(request):
    logout(request)
    return redirect(home)

def contact_form(request):
    form = ContactForm()
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact_data = Contactinfo(name=name,email=email,message=message)
            contact_data.save() 
            context['success'] = "Thank you! Your message has been successfully sent. ..."
    context['form'] = form
    return render(request,'signupform/contact.html',context)

def user_image_posted(request):

    if request.method == "POST":
        postform = UserUploadedPostForm(request.POST,request.FILES)
        if postform.is_valid():
           print(request.FILES['post_image'])
        return redirect(home)
    return render(request,'home.html')