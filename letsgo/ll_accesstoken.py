import requests
import json
from .models import User_details

aid=2883115551953125
asecret='352a87e92cb615c2173895e10b69f1c4'
def get_atoken(usertoken):
    print(type(usertoken),usertoken)
    ll_usertoken='https://graph.facebook.com/v6.0/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}'.format(aid,asecret,usertoken)
    
    r=requests.get(ll_usertoken)
    print(r.text)
    print(type(r))
    r=r.json()
    ll_accesstoken=r["access_token"]
    # print(ll_accesstoken)
    userid='https://graph.facebook.com/v6.0/me?access_token={}'.format(ll_accesstoken)
    r1=requests.get(userid)
    # print(r1.text)
    r1=r1.json()
    user_id=r1["id"]
    # print(user_id)
    ll_pagetoken='https://graph.facebook.com/{}/accounts?access_token={}'.format(user_id,ll_accesstoken)
    r2=requests.get(ll_pagetoken)
    # print(r2.text)
    r2=r2.json()
    # global atoken
    # global page_id
    atoken=r2['data'][0]['access_token']
    page_id=r2['data'][0]['id']
    user_name=r2['data'][0]['name']
    order=User_details(user_name=user_name,page_id=page_id,access_token=atoken)
    order.save()
    

# get_atoken() 
# print(atoken)   