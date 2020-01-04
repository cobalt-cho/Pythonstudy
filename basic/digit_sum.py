'''
정수 안의 각 자리수의 합을 계산
EX) 1234가 입력되면 1+2+3+4 = 10
    10 출력
'''

n = int(input("input the digit number : "))

sum = 0
while(n>0) :
    a = n%10
    sum += a
    n = n//10

print(sum)