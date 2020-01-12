# list using

value = [1,2,3] * 3
print(value) # 1,2,3,1,2,3,1,2,3

letters = ['a','b','c','d']
len(letters) # 4

# list 끝에 추가
shoppinng_list = []
shoppinng_list.append("cookie")
shoppinng_list.append("tuna")
shoppinng_list.append("banana")

# 1번 index에 water 추가
shoppinng_list.insert(1,'water')

apple = ['ipot','iphone','ipad','watch','airpot']

# 요소가 있나 확인
if 'airpot' in apple :
    print("airpot in my pocket")

# 요소 삭제
apple.pop(1) # 1번 index 항목 삭제 및 반환

# remove()
apple.remove("ipad") # 항목을 받아서 제거, 반환 X

# sort() : in-place sort
a = [3,2,1,5,4]
a.sort()
print(a) # 1,2,3,4,5

# sorted() : 정렬된 새로운 리스트 반환
b = [3,2,1,5,4]
c = sorted(b)
print(c) # 1,2,3,4,5

d = sorted(b,reverse = True)
print(d) # 5,4,3,2,1

word=  sorted("A picture is worth a thousand words.".split())
print(word)

# finding index
print(word.index("A")) # 0
# print(word.index('d')) list에 존재하지 않을시 오류발생 !

'''
list copy
-> 리스트 변수는 객체를 직접 저장X, 리스트 자체는 다른 곳에 저장되고
   참조값만 변수에 저장된다. (참조값은 위치를 말한다)
'''

scores = [40,63,22,89,29,39,68]
values = scores # shallow copy
values[2] = 999
print(scores) # 둘 다 같은 곳을 참조하므로 하나만 변경해도 값은 전부 변경됨!

scores2= [23,92,76,72,51]
values2 = list(scores2) # deep copy, deepcopy(scores2)
values2[2] = 1000
print(scores2)

# 리스트 함축(list comprehensions)
s = [x**2 for x in range(10)] # 간결하게 표현 가능
list1 = ['all','good','anything','please']
item = [i[0] for i in list1]

# 이차원 리스트
s = [[1,2,3,4,5],[4,5,6,7],[8,9,10,11,12,13]]

rows = 6
cols =6
table = []

for row in range(rows):
    table+= [[0]*cols]


