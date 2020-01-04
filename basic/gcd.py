'''
최대공약수 구하기(유클리드)
이해가 안되서 그냥 외웠다.
'''

x = int(input("정수 입력(큰 수)"))
y = int(input("정수 입력(작은 수)"))

while(y!=0):
    r = x%y
    x,y = y,r # python은 swap과정을 이런 방법으로 쉽게 가능.

print("최대 공약수 :" ,x)
