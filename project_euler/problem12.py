'''
500개 이상의 약수를 갖는 가장 작은 삼각수는?
삼각수 : 1부터 n까지의 자연수를 차례로 더하여 구해진 값을 삼각수라고 한다
Ex) 7번 째 삼각수는 1+2+3+4+5+6+7 = 28
1,3,10,15,21,28,36,45,55 ...
미완성
'''

li = list(range(1,100000))

sum=0
li2 = []
for i in li :
    sum+=i
    for j in range(2,sum):
        if j>sum / i :
            break
        if sum % j== 0:
            li2.append(j)
            if sum//j!=j:
                li2.append(sum//j)
    if len(li2)>=500:
        print(sum)
        break