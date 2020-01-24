import os
import sys
import requests
from pprint import pprint
import json
client_id = "WnIkLbCnPw9wvIys7MjX"
client_secret = "OGjfLWFl6x"
#url = "https://openapi.naver.com/v1/vision/face"    #얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" #유명인 얼굴인식
files = {'image': open('27.JPG', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

# json : 문자열로 데이터, 객체 정보를 문자열로 표현하는 형식
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
if(rescode==200):
    #print (response.text)
    data = json.loads(response.text) # dictionary 형태로 변환
    pprint(data)
    print(data['info']['faceCount'])
else:
    print("Error Code:" + rescode)