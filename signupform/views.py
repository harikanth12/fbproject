from django.shortcuts import render,redirect
from signupform.forms import SignupForm,ContactForm,UserUploadedPostForm,EditForm
from signupform.models import Userinfo,Contactinfo,UserPostedImages,Likecount
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
import time
from django.contrib import messages

# Create your views here.
def signupform(request):
    context = {}
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
            context['success'] = "Your account created successfully!!!You can log in now!!!"

    else:
        form = SignupForm()
    context['form'] = form
    return render(request,'signupform/signupform.html',context)

def home(request):
    context = {}
    user_posted_data = UserPostedImages.objects.all().order_by('-id')[:10]
    # print(user_posted_data.post_image.url)
    context['data'] = user_posted_data
    return render(request,'home.html',context)

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
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            name1 = form.cleaned_data['username']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name1,email,message)
            contact_data = Contactinfo(name=name1,email=email,message=message)
            contact_data.save() 
            context['success'] = "Thank you! Your message has been successfully sent. ..."
    else:
        form = ContactForm()
    context['form'] = form
    return render(request,'signupform/contact.html',context)

def user_image_posted(request):

    if request.method == "POST":
        postform = UserUploadedPostForm(request.POST,request.FILES)
        folder = 'media/uploaded_images/'
        if postform.is_valid():
            print(request.FILES['post_image'])
            # print(request.FILES['post_image'])
            post_image1=request.FILES['post_image']
            # timestamp = time.time()
            # print(type(post_image1))
            fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
            a = fs.save(post_image1.name,post_image1)
            
            # sfinal_post_image = str(post_image1) + str(timestamp)
            posted_image_data = UserPostedImages(username=request.user.username,post_image='uploaded_images/'+a)
            posted_image_data.save()
            messages.success(request, 'your Uploaded Post Successfully') 
        return redirect(home)
    return render(request,'home.html')

def edit_profile(request,id=None):
    context = {}
    user_data = User.objects.get(id=id)
    user_info = Userinfo.objects.get(user=user_data)
    context['profiledata']=user_data
    context['userinfo'] = user_info
    context['success'] = None
    form = EditForm()
    if request.method == "POST":
        form = EditForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            # print("dkjvjzj vk")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            MobileNumber = form.cleaned_data['MobileNumber']
            Address = form.cleaned_data['Address']
            DateOfBirth =form.cleaned_data['DateOfBirth']
            user_data = User.objects.filter(id = id).update(username=name,email=email)
            
        ## for one to one field ..for reference we have to pass the User Instance thats means user_data
            user_info = Userinfo.objects.filter(user=user_data).update(mobilenumber=MobileNumber,address=Address,dob=DateOfBirth)
            messages.success(request, 'Changes successfully saved.')
            return redirect(edit_profile,id=id)
    return render(request,'signupform/edit_profile.html',context)

def post_like(request,post_id=None,user_id=None):
    print(post_id,user_id)
    user_name = User.objects.get(id=user_id)
    post_data = UserPostedImages.objects.get(id=int(post_id))

    count = 0
    try:
        oldcount = Likecount.objects.get(post_image_id_id=post_id,username=user_name.username)
        if oldcount.like_count == 1:
            count = oldcount.like_count - 1
            Likecount.objects.filter(post_image_id_id=post_id,username=user_name.username).update(like_count = count)
            UserPostedImages.objects.filter(id=post_id).update(like = post_data.like -1 )
        else:
            count = oldcount.like_count + 1
            Likecount.objects.filter(post_image_id_id=post_id,username=user_name.username).update(like_count = count)
            UserPostedImages.objects.filter(id=post_id).update(like = post_data.like + 1)
    except  Likecount.DoesNotExist:
        new_count= Likecount.objects.create(post_image_id_id=post_id,username=user_name.username,like_count=1)
        new_count.save()
        UserPostedImages.objects.filter(id=post_id).update(like = post_data.like + 1)
    
    return redirect(home) 
    
    

    
    # count_like = Likecount(post_image_id = post_data,username=user_name)
    