'''
500개 이상의 약수를 갖는 가장 작은 삼각수는?
삼각수 : 1부터 n까지의 자연수를 차례로 더하여 구해진 값을 삼각수라고 한다
Ex) 7번 째 삼각수는 1+2+3+4+5+6+7 = 28
1,3,10,15,21,28,36,45,55 ...

약수들을 구하는 방식 => 속도가 오래 걸려 유튜브를 참고함.

리스트를 for문 밖에 두어서 계속 누적되게 하는 실수를 했다.
for문 안에 넣으니 결과를 잘 나타냄
'''

li = list(range(1,100000))

sum=0

for i in li :
    li2 = []
    sum+=i
    for j in range(2,sum):
        if j > sum/j : # 반복되는 약수 계산을 하지 않기 위해서
            break
        if sum % j== 0:
            li2.append(j) # 나머지가 0인 수를 append
            if sum//j!=j: # 제곱수를 한번만 넣기 위해 EX) 49 , 7
                li2.append(sum//j)
    if len(li2)+2>=500:
        print(sum)
        break