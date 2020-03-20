from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.

def register(request):

    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This email is already in use")
                return redirect('register')
            else:
                user= User.objects.create_user(password=password1,username=username,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'user created')
                return redirect('signin')
        else:
            messages.info(request,"user password not mathched")
            return redirect('register')
    else:
        return render(request,"register.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials !!!")
            return redirect('signin')
    else:
        return render(request,"signin.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def profile(request):
    return render(request,'profile.html')