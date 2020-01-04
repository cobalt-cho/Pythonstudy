'''
"우리가 함수의 내부에서 변수 s에 값을 저장하면 파이썬은
우리가 지역 변수 s를 정의한 것으로 생각한다" -> 전역변수 s가 아닌 것이다

함수 안에서 변수에 어떤 값을 저장하면 무조건 지역 변수로 간주 -> default가 지역 변수

** 함수 안에서 하나의 변수가 전역 변수도 되었다가 지역 변수도 될 수 없는 것이다.

'''
def sub() :
    s = "I like pizza !"
    print(s)

s = "I like chicken"
sub()
print(s)
print()

'''
함수 안에서 전역 변수의 값을 변경해야 되겠다면 global 사용 -> 전역 변수를 사용하겠다고 interpreter에게 알려야 함.
'''

def sub2():
    global a # 함수 안에서 전역변수 s 사용
    print(a)
    a = "I like apple !" # 전역변수 변경
    print(a)

a = "I like banana !"
sub2()
print(a)