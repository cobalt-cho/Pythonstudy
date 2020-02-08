'''
2^1000의 자리수를 모두 더하면?
'''

n = 2**1000

sum = 0
while n!=0 :
    sum+=n%10
    n = n//10

print(sum)