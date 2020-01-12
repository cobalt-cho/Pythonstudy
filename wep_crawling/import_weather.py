from bs4 import BeautifulSoup as bs
from pprint import pprint
# list,dictionary 같은 것들이 길 때 정리해서 보여줌
import requests
# URL을 적으면 그 페이지에 대한 소스코드 볼 수 있음

# 네이버 날씨는 나의 위치를 알아서 알려줌
html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = bs(html.text,'html.parser') #parsing
#pprint(soup)

#HTML 요소
'''
태그 : div
속성 : class
속성값 : detail_box
'''

data1 = soup.find('div',{'class': 'detail_box'})
# 소스에 여러개의 속성이나 태그가 있을 경우 맨 첫 번째만 반환
#pprint(data1)

# findAll - 모두 탐색을 하는것
data2 = data1.findAll('dd') # list로 반환
#pprint(data2)

find_dust = data2[0].find('span',{'class':'num'})
pprint(find_dust.text)