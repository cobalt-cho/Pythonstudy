'''
python의 여러가지 자료구조
'''

# tuple : 튜플의 내용은 변경될 수 없다.
print("**tuple")

colors = ('red','green','blue')
numbers = (1,2,3,4,5)
t = ('hello',1,3)
a = (10) # 정수
print(type(a))
a = (10,) # tuple
print(type(a))

all = colors + numbers
print(all)
c = (3,6,9)
t1 = 1,2,4,'a','b' # tuple로 간주

# set : 항목간 순서 X, 중복 X, 요소 인덱싱, 슬라이싱 불가
print()
print("**set")

z = set([1,2,3,1,2,3])
print('z =',z)
z.add(5) # 1개만 추가 가능
z.update([7,8,9]) # 여러 요소 추가 가능, iterable 요소 넣는다
z.discard(11) # 삭제
z.remove(3) # 제거 할 때 set에 없으 시 예외발생
z.clear() # 전체 요소 지우기
A = {1,2,3}
B = {1,2,3}
print(A==B)
A = {1,2,3,4,5}
B = {1,2,3}
B.issuperset(A)
A.issubset((B))

# 딕셔너리 : key : value 존재
# key는 변경불가능한 객체(문자열,숫자)
print()
print("**dictionary")

d = {} # 공백 딕셔너리
d = {1:'apple',2:'banana'}
print(d[1])
print(d.get(1))
if 1 in d :
    print("Key 존재")
d[3] = 'grape' # 추가
print(d)
d.pop(1) # 제거 또는 del 사용

