'''
100!의 자리수를 모두 더하면?

'''

fac = 1
for i in range(2,101):
    fac*=i

sum = 0
while fac !=0 :
    sum += fac%10
    fac = fac//10


print(sum)
