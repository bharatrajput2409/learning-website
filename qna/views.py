from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from .models import materials
from .models import comments
from .models import mat_solutions
from datetime import datetime
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")
def contact(request):
    return render(request,"contact.html")
def upload(request):
    return render(request,"upload.html")

def download(request):
    return  render(request,"download.html")
def  material(request):
    ccode=request.GET['ccode']
    mats=materials.objects.order_by('-id').filter(ccode=ccode)
    comment=comments.objects.order_by('-id').filter(ccode=ccode)
    sol=mat_solutions.objects.order_by('-id').filter(ccode=ccode)
    return render(request,"material.html",{'mats':mats,'ccode':ccode,'comment':comment,'sol':sol})



def addcomment(request):
    obj=comments()
    obj.uploader_name=request.POST['username']
    obj.ccode=request.POST['ccode']
    obj.comment=request.POST['comment_data']
    obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def upload_solution(request):
     obj=mat_solutions();
     obj.uploader_name=request.POST['username']
     if(obj.uploader_name==""):
        messages.info(request,"!!! login to upload solutions !!!")
        return redirect('signin')
     obj.mat_id=request.POST['mat_id']
     obj.img="pics/" + request.POST['img_file']
     obj.ccode=request.POST['ccode']
     obj.save()
     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def upload_mat(request):

    obj=materials();
    obj.uploader_name=request.POST['username']
    if(obj.uploader_name==""):
        messages.info(request,"!!! login to upload materail !!!")
        return redirect('signin')
    obj.img="pics/" + request.POST['img_file']
    obj.ccode=request.POST['ccode']
    obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))