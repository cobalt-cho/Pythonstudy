'''
random 모듈
'''
import random

print(random.random()) # 0 이상 1미만 숫자
print(random.randrange(1,7)) # 1~6 숫자
print(random.randint(1,7)) # 1~7 숫자
print(random.uniform(1,9)) # 1~9 숫자 (실수)

# shuffle() : sequence 자료형을 섞음
a= [1,2,3,4,5]
random.shuffle(a)
print(a)

# choice() : 아무 원소나 뽑음
print(random.choice(a))

#sample() : (seq or set, N), N개만큼 유니크한 요소 뽑기
print(random.sample(range(46),6))
print(random.sample('faaaga',6))
print(random.sample('aaaaaaaaa',5)) # 다 같은 a가 아니라 위치가 다른 a

