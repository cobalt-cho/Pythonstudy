'''

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
(1 = 14의 경우는 엄밀히 말해 합이 아니므로 제외합니다)

위의 세 숫자를 모두 더하면 1634 + 8208 + 9474 = 19316 입니다.

그렇다면, 각 자리 숫자를 5제곱해서 더했을 때 자기 자신이 되는 수들의 합은 얼마입니까?

'''

li = []
# 범위를 어디까지 잡아야 할 지 모르겠다.
for i in range(1,1000000):
    su = sum(int(j)**5 for j in str(i))
    if su == i :
        li.append(i)

print(sum(li)-1) # 1은 포함하지 않으므로 1 빼줌

