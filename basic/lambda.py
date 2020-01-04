'''
 lambda 함수
 -> 여러 개의 인수를 가질 수 있으나 반환값은 하나만 !
 -> print()를 호출 불가능, 계산만 가능
 -> 전역변수 참조 불가능
 -> return 키워드 사용 X

'''

# EX.01
sum = lambda x,y,:x+y;
print(sum(10,20))
print(sum(30,40),"\n")

def get_sum(x,y):
    return x+y

print(get_sum(10,20))
print(get_sum(30,40),"\n")

# EX.02
L = [lambda x : x**2,lambda x: x**3,lambda x : x**4]
for i in L :
    print(i(3))

# EX.03
min = (lambda x,y :x if x>y  else y)