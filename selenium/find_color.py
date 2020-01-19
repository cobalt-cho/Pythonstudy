from selenium import webdriver
from pprint import pprint
import time
from collections import Counter

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

# xpath 찾기
btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
#print(len(btns))

# btns에서 css 컬러값을 리스트로 저장
btns_rgba = [ btn.value_of_css_property('background-color') for btn in btns]
#pprint(btns_rgba)

result = Counter(btns_rgba) #dictionary처럼 rgb값을 보여줌
pprint(result) #여기서 value가 1인게 정답(다른 색을 찾는 것이기 때문에)

#value가 1인 것 탐색
for key, value in result.items():
    if value == 1:
        answer = key
        break
else:
    answer = None
    print("정답을 찾을 수 없습니다.")