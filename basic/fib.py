'''
피보나치 수열을 재귀적으로 구성 시
똑같은 연산을 계속함
->그 값들을 dictionary에 저장하여 불러와 해결함
'''

table = {0:0,1:1}

# n번 째 피보나치 수열 값을 찾음
def fib(n):
    if n not in table :
        value = fib(n-1) + fib(n-2)
        table[n] = value
    return table[n]

print(fib(100))