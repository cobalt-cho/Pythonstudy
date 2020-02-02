'''
10001번째의 소수
나오긴 하는데 너무 느리다.
속도를 어떻게 하면 빨리 할 수 있을까...?
'''


def Prime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

n=0
answer= 0
for i in range(1,100000000):
    if(Prime(i)):
        n+=1
        if n==10001:
            answer = i
            break
print(answer)












