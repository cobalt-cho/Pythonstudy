'''

세자리 수를 곱해 만들 수 있는 가장 큰 대칭수

두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는
9009(91X99)일 때 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수

'''

'''
999*999가 6자리가 나왔기 때문에 이런식으로 간단히 하였다
좀 더 일반적인 경우를 생각해서 다시 해봐야함.
'''

li = []
for i in range(100,1000):
    for j in range(100,1000):
        a = str(i*j)
        if len(a) == 6 :
            if a[0]==a[5] and a[1]==a[4] and a[2] == a[3] :
                li.append(a)

print(max(li))