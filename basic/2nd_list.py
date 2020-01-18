'''
2차원 리스트
'''

# 동적으로 2차원 리스트 생성

rows = 3
cols = 5
s = [ ]

for row in range(rows) :
    s+=[[0]*cols]

#print(s)

# 2차원 리스트 접근

s = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

rows = len(s)
cols = len(s[0])

for r in range(rows):
    for c in range(cols):
        print(s[r][c],end =" ")
    print()

# 2차원 리스트 연산

cols =len(s[0])
sum = 0
for c in range(cols):
    sum= sum + s[1][c]

print(sum)
