# 지뢰판 만들기
import random

board = [[False for x in range(10)] for y in range(10)]

for r in range(10):
    for c in range(10):
        if(random.random() < 0.3): # 난수발생 30% 확률로 지뢰 생성 #이 지뢰
            board[r][c] = True

for r in range(10):
    for c in range(10):
        if board[r][c] == True :
            print('#',end =' ')
        else :
            print('.',end=' ')
    print()

