from django.shortcuts import render
from django.http import HttpResponse
import facebook
import requests
from . import combined
# Create your views here.
def index(request):
     thank=False
     if request.method=="POST" :
        page_id=request.POST.get('name','')
        msg=request.POST.get('msg','')
        combined.post_status(page_id,msg)

     return render(request,"index.html",{'thank':thank})
    
def status(request):
   return render(request,"status.html")


def postimg(request):
   if request.method=="POST" :
       fb_id=request.POST.get('name','')
       insta_id=request.POST.get('instaid','')
       img_url=request.POST.get('img','')
       msg=request.POST.get('msg','')
       combined.post_img(fb_id,img_url,msg)
       combined.insta_post(insta_id,img_url,msg)
   return render(request,"imagepost.html")