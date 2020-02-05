'''
이백만 이하 소수의 합

지금까지 구해왔던 소수로는 시간이 너무 오래 걸려
에라토스테네스의 체를 사용하니 시간이 엄청나게 빠르다.
'''

# 에라토스테네스의 체
def prime(n):
    # 에라토스테네스의 체로 n개 요소에 True 설정 소수라 생각.
    primeList = [True] * n
    answer = []

    # n의 최대 약수가 sqrt(n) 이하라서 sqrt(n)까지만 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if primeList[i] == True: # i가 소수인 경우
            for j in range(i+i, n, i): # i의 배수들을 False 판정
                primeList[j] = False

    # True가 소수이므로 True index만 다른 리스트에 저장장
    for i in range(2,n):
        if primeList[i] == True :
            answer.append(i)

    return answer

print(sum(prime(2000000)))







