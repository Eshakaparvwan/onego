import requests
import json

 

# page_id=109214341345652
itoken='EAAoZBLaZASEOUBAPmxBoBtEA3E9zf6PoJ534E6vwxuBbQWm9e9WwS4o4egEMxhdDzL885ZA8jhN7QWRD58pBmaffuvJutMS7VZCaNL4JLGfYiqfTfq8UNfpfQ08oswbE4grQnej3jLmz594ZBwwH70sOJS54OCRdSA4g3mgw00spYMEZBZATgZABlooNpzvCqJlKZB9cOzAZAanRIDpnleZC7ZBORtT9Tbkr3nDJxC0GRboZCtp6ikMmuh06B'
# atoken='EAAoZBLaZASEOUBABQ2UCbhyIIOocwqLETNVaPzfjSbQtHZAVrqSncmqwLPqhdqTcJDalDh0wanpyH10a4FMKY0ro8kteYcysq3Jpf3py0cNpgc0DZCOt1QWPGZCGiPZB47oquqZCjozniZBds31aRZA50ZAADlVayVZB0SsfgsA2uAD9MlX8czyj69MZAZCMGUqqTuABHUQEdfEs1g5QcLDJT6icu'

def post_img(fb_id,img_url,msg,atoken):
    msg=msg
    page_id=fb_id
    image_url='https://graph.facebook.com/{}/photos'.format(page_id)
    image_loc=img_url
    img_payload={
    'message':msg,
    'url':image_loc,
    'access_token':atoken,

    }
    r=requests.post(image_url,data=img_payload)
    print(r.text)
    # insta_post()

def post_status(page_id,msg,token):
    # print(type(atoken),type(token),type(page_id))
    atoken=token
    print(atoken)
    # print(token)
    # page_id=page_id
    post_url='https://graph.facebook.com/{}/feed'.format(page_id)
    
    mesg=msg
    payload={
             'message':msg,
             'access_token':atoken,
               }  
    r=requests.post(post_url,data=payload)
    print(r.text)

def insta_post(insta_id,img_url,msg):
    # image_location_1='https://image.freepik.com/free-vector/software-development-programming-language-coding_284092-33.jpg'
    # ig_user_id=17841447918290784
    msg=msg
    ig_user_id=insta_id
    image_location_1=img_url
    post_url='https://graph.facebook.com/v10.0/{}/media'.format(ig_user_id)
    payload = {
          'image_url':image_location_1,
          'caption':msg,
          'access_token':itoken,

             }  
    r=requests.post(post_url,data=payload)
    print(r.text)
    result=json.loads(r.text)
    if 'id' in result:
        creation_id=result['id']
    # second_url='https://graph.facebook.com/v10.0/{}/media.publish'.format(ig_user_id)
        second_url='https://graph.facebook.com/{}/media_publish'.format(ig_user_id)
        second_payload={
             'message':msg,
             'creation_id':creation_id,
             'access_token':itoken
        }
        r=requests.post(second_url,data=second_payload)
        print(r.text)
    else:
        print("we have problm")
