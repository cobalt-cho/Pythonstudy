'''
문자열의 중앙에 있는 문자 출력
"weekday"라면 "k" 출력
"string"처럼 짝수라면 "ri" 출력
'''

str =input("문자입력 :")

if len(str)%2==1:
    print(str[len(str)//2])
else :
    print(str[(len(str)//2)-1],str[len(str)//2])