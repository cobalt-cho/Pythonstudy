'''
행렬 만들기
-> 2차원 리스트를 사용하면 0을 만들 때 메모리 낭비가 심함
-> dictionary로 저장 0 : 0이 아닌 값만 저장한다
'''

matrix = {(1,2):1,(2,2):2,(3,2):3}

for x in range(5):
    for y in range(5):
        print(matrix.get((x,y),0), end = ' ')
    print()