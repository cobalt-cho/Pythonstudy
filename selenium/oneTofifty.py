from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300) # selenium에서 쓰는 time

#전역변수
#현재 찾아야될 숫자
num = 1

def clickBtn():
    global num
    # div[*]로 해당요소를 전부 찾는다
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        print(btn.text, end='\t') # 누를 text를 보여줌
        if btn.text == str(num):
            btn.click() # 같은 숫자를 찾으면 click
            print(True)
            num += 1
            return

while num<=50:
    clickBtn()