'''

피보나치 수열에서 처음으로
1000자리가 되는 항은 몇 번째?

'''

a,b = 1,1
li = []
cnt = 2
while True :
    n = a+b
    a,b =b,n
    cnt += 1 # 몇 번째 항을 구할 때 1이 자꾸 크다 이유를 찾자.
    if len(str(a))-1 >= 1000   :
        print(cnt)
        break
