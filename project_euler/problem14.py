'''
양의 정수 n에 대하여 다음과 같은 계산 과정을 반복
n -> n/2  (n짝수)
n -> 3n+1 (n홀수)

EX) 13에 대해 10번 과정을 통해 1
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 ->1

백만 이하의 수로 시작했을 때 1까지 도달하는 데
가장 긴 과정을 거치는 숫자는?
(계산 과전 도중에 숫자가 백만을 넘어도 됨)

시간이 오래걸린다 시간을 줄여야 한다
'''


def solve(n):
    cnt=1
    while n!=1:
        if n%2==0:
            n = n/2
            cnt+=1
        else :
            n = 3*n+1
            cnt+=1
    return cnt

max = 0
answer = 0
for i in range(1,1000000):
    if  max < solve(i):
        max = solve(i)
        answer=i

print(answer)

