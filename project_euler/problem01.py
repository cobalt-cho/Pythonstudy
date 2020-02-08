# 1000보다 작은 자연수 중에서 3 또는 5의 배수 더하기

sum = 0

for i in range(3,1000):
    if i%3==0 or i%5==0 :
        sum +=i
print(sum)