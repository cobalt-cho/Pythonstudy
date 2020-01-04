'''
프로그래밍 언어에서 일반적으로 사용하는 함수 인자 전달 방식
1. Call by value
2. call by reference
** 숫자나 문자열이 변경 불가능한 객체(immutable object)

call by value : 값에 의한 호출, 즉 값이 지정된 변수를
                인자로 넘기는 것이 아니라 변수에 할당된 값만 복사하여
                함수의 인자로 넘기는 방식
'''
def callA(value) :
    print(value)
a = 2
callA(a)
'''
a를 함수의 parameter로 넘겼을 때 a가 넘어간 게 아니라 2가
memory에서 복사되어 value에 할당

callA라는 함수 내부에서 a의 값을 넘겨 받은 value의 값을
변경하더라도 a의 값은 변하지 않는다.

같은 2라는 값을 가졌어도 a의2와 value의 2는 
다른 위치의 memory에 저장되어 있음.
'''
