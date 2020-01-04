'''
윤년 구하기
조건 1) 4로 나누어지며 100으로 나누어지지 않으면 윤년
조건 2) 400으로 나누어지면 윤년

'''
year = int(input("input the year"))

answer = True

if year%4==0 and(year%100!=0 or year%400==0) :
    answer = True
    print(answer)
else :
    answer = False
    print(answer)
