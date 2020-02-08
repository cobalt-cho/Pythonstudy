'''
a+b+c=1000이 되는 피타고라스 수
'''
import math

def pita():
    sum = 0
    for i in range(1,1000):
        for j in range(1,1000):
            n = (i*i)+(j*j)
            k = math.sqrt(n)
            if(1000-(i+j+k)==0):
                return i*j*k


print(int(pita()))
















