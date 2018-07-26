import requests
import json
import cv2
import sys

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

