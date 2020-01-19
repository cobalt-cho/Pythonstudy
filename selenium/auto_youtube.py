from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver') # 다른 디렉토리에 존재 시 경로 작성
driver.get("https://www.youtube.com/") # 홈페이지를 연다

time.sleep(3)

#검색어 창의 xpath를 찾아 search에 저장
search = driver.find_element_by_xpath('//*[@id="search"]')


search.send_keys('반원 코딩') # 키워드 입력
time.sleep(1)

search.send_keys(Keys.ENTER) # enter로 검색