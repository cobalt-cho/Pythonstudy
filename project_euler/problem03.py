'''
가장 큰 소인수 찾기

-> 1부터 차례대로 for문으로 하면
   숫자가 어느정도 커지면 넘어가지 않음
-> 소수들을 list에 담는다

-> 나누어 떨어지는 수까지만 본다?
-> 제곱근까지만 나눈다.

'''
primes = []
n = 600851475143
f = 2

while n!=1:
    if(n%f==0):
        primes.append(f)
        n/=f
    else:
        f+=1
print(max(primes))
