from bs4 import BeautifulSoup as bs
from pprint import pprint

import requests


html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = bs(html.text, 'html.parser')

data1_list = soup.findAll('div',{'class':'col_inner'})
#print(len(data1_list)) 요일별로 묶는다

# 전체 웹툰 리스트
week_title_list = []
for data1 in data1_list :
    data2 = data1.findAll('a',{'class':'title'})
    title_list = [t.text for t in data2]
    week_title_list.append(title_list) # 이중 리스트의 형태로 저장
    #week_title_list.extend(title_list) #리스트에 바로 저장 (단일 리스트)

pprint(week_title_list)


