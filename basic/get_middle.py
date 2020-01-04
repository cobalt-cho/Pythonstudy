'''

if문은 block으로 속해 있는 부분을 전부 실행한다.
4칸 indentation
계속 동일한 공백으로 작성하고 안에 if문이 또 들어갈 시 if문 안에
다시 indentation.



문자열의 중앙에 있는 문자 출력
"weekday"라면 "k" 출력
"string"처럼 짝수라면 "ri" 출력
'''

str =input("문자입력 :")

if len(str)%2==1:
    print(str[len(str)//2])
else :
    print(str[(len(str)//2)-1],str[len(str)//2])