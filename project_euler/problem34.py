'''

숫자 145에는 신기한 성질이 있습니다. 각 자릿수의 팩토리얼(계승)을 더하면  1! + 4! + 5! = 1 + 24 + 120 = 145 처럼 자기 자신이 됩니다.

이렇게 각 자릿수의 팩토리얼을 더하면 자기 자신이 되는 모든 수의 합을 구하세요.

단, 1! = 1 과 2! = 2 의 경우는 덧셈이 아니므로 제외합니다.

속도를 늘려야 한다. 느림.
'''

li = []
for a in range(3, 1000000):
    a2= a
    sum = 0
    while a != 0:
        fact = 1
        b = a % 10
        a = a // 10
        for i in range(2, b + 1):
            fact *= i
        sum += fact
    if sum == a2 :
        li.append(a2)

sum = 0
for i in li :
    sum+=i

print(sum)
