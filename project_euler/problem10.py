'''
이백만 이하 소수의 합
'''

sum = 0

def Prime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

for i in range(2,2000000):
    if(Prime(i)):
        sum+=i
print(sum)















