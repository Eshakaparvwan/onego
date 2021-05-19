import requests
import json

# page_id=109214341345652
itoken='EAAoZBLaZASEOUBANW5eA5O8V2YtpEckgIoeKdffuRgwAsiLi8ZAvZBQuBOTnfFMS0LCJVEUGKzYV7X7caKZCa2p1Wm2r8Ejo22YzIDGbWibmTO0peZCg2diq05uyZB0pxajYATwOXqP6si4ZBTwru7sRxIZATLjXUge9JZA8yjzd1t6cS1KxZCgwP07cvw6d19MpsoQvb3el1f0iJrkZALRZBLv4Ne3EqCY2koX0ogqE8mtFRAhitl2lIIcUoOquPIZAZAHhmIZD'
atoken='EAAoZBLaZASEOUBADSoHXZC0AoR6uj4Xl5GFZByzr9JSAgzbIyZBedtoN1yIIBdtmOgQ60xZB3c7s4UyC985Q9BQTOoZAMT83xJvEV4iJDhNpBxCaywRSsT4ZBFlz7NvhC9UIOTdFst6fArDXU3dh5RYgYi67PWTvDp39FuEU969KMqNFvgZBhVaFLSt1IrruGI65hUYoq9jnkQGoMY70uWrsb'

def post_img(fb_id,img_url,msg):
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

def post_status(page_id,msg):
    page_id=page_id
    post_url='https://graph.facebook.com/{}/feed'.format(page_id)
    mesg=msg
    payload={
             'message':msg,
             'access_token':atoken
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
    