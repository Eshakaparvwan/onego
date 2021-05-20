from django.shortcuts import render
from django.http import HttpResponse
import facebook
import requests
from . import combined,ll_accesstoken
from .models import User_details
# Create your views here.
def index(request):
     thank=False
     if request.method=="POST" :
        
        page_name=request.POST.get('name','')
        msg=request.POST.get('msg','')
       
        
        prod=User_details.objects.filter(user_name=page_name)
        q=prod.values('user_name','page_id','access_token')
        page_id= q[0]['page_id']
        atoken=q[0]['access_token']
        print(page_id,atoken)
        combined.post_status(page_id,msg,atoken)

     return render(request,"index.html",{'thank':thank})
    
def status(request):
   if request.method=="POST" :
        user_token=request.POST.get('fblogin','')
        print(user_token)
        ll_accesstoken.get_atoken(user_token)
   return render(request,"status.html")


def postimg(request):
   if request.method=="POST" :
       fb_id=request.POST.get('name','')
       insta_id=request.POST.get('instaid','')
       img_url=request.POST.get('img','')
       msg=request.POST.get('msg','')
       prod=User_details.objects.filter(page_id=fb_id)
       q=prod.values('user_name','page_id','access_token')
       page_id= q[0]['page_id']
       atoken=q[0]['access_token']
       combined.post_img(page_id,img_url,msg,atoken)
       combined.insta_post(insta_id,img_url,msg)
   return render(request,"imagepost.html")