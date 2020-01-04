'''
python은 어떤 자료형이 데이터도 저장할 수 있다.
파이썬에서는 모든 것이 객체로 되어 있기 때문
따라서 객체이기만 하면 뭐든지 변수로 가리킬 수 있다

연산자 우선 순위
지수 >곱셉,나눗셈,나머지 > 덧셈,뺄셈

* 파이썬 여러 개 input 방법 !
    1. a,b = input().split()
    2. a,b = map(int, input().split())
'''

# 자동 판매기

price = int(input("물건 값"))

coin50000 = int(input("50000원 의 수 : "))
coin10000 = int(input("10000원 의 수 :"))
coin5000 =  int(input("5000원 의 수 :"))
coin1000 =  int(input("1000원 의 수 :"))
coin500 =   int(input("500원 의 수 :"))
coin100 =   int(input("100원 의 수 :"))
totalCoin = coin100*100 + coin500*500 + coin1000*1000 + coin5000*5000 +  coin10000*10000 + coin50000*50000
change = totalCoin - price

change50000 = change//50000
change = change%50000

change10000 = change//10000
change = change%10000

change5000 = change//5000
change = change%5000

change1000 = change//1000
change = change%1000

change500 = change//500
change = change%500

change100 = change//100
change = change%100

change50 = change//50
change = change%50

change10 = change//10
change = change%10

print()
print("잔 돈")
print("--------------------------")
print("5만원 : ", change50000)
print("1만원 : ", change10000)
print("5천원 : ", change5000)
print("1천원 : ", change1000)
print("5백원 : ", change500)
print("100원 : ", change100)
print("50원 : ", change50)
print("10원 : ", change10)



