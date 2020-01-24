# 네이버 Papago NMT API 예제
import os
import sys
import json
from pprint import pprint
import urllib.request

# 번역 할 메모장 불러오기
with open('source.txt', encoding='utf-8') as f:
    srcText = f.read()

client_id = "WnIkLbCnPw9wvIys7MjX"
client_secret = "OGjfLWFl6x"
encText = urllib.parse.quote(srcText) # 번역 할 내용

data = "source=ko&target=ja&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    #print(response_body.decode('utf-8'))
    res = json.loads(response_body.decode('utf-8'))
    pprint(res)

    # 파일 생성
    with  open("translate.txt",'w',encoding='utf-8') as f:
        f.write(res['message']['result']['translatedText'])
else:
    print("Error Code:" + rescode)