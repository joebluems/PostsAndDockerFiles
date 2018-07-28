import requests
import json
import cv2
import sys
import tweepy

#### twitter setup ####
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

cfg = { 
    "consumer_key"        : "...",
    "consumer_secret"     : "...",
    "access_token"        : "...",
    "access_token_secret" : "..." 
    }
api = get_api(cfg)

if len(sys.argv)!=4:
  print("Usage: python",sys.argv[0]," <IMAGE> <IP> <PORT> ")
  sys.exit(0)

URL = "http://%s:%s/api/test" % (sys.argv[2],sys.argv[3])

### prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

### read image and send request ###
img = cv2.imread(sys.argv[1])
_, img_encoded = cv2.imencode('.jpg', img)
response = requests.post(URL, data=img_encoded.tostring(), headers=headers)

### print response ###
print(response.json())
tweet = response.json()
image = sys.argv[1]
status = api.update_with_media(image, status=tweet) 

