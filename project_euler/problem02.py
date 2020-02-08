# 피보나치 수열에서 4백만 이하이면서 짝수인 항의 합

a,b =1,2

sum = 0
while a<=4000000 :
    n = a+b
    a,b =b,n
    if a%2==0 :
        sum+=a

print(sum)