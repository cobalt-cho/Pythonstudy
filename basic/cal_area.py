'''
선택하는 도형의 면적을 계산하는 프로그램
'''

choice = int(input("1.rectangle 2.triangle 3.circle :"  ))

if (choice == 1) :
    width = int(input('width :'))
    length = int(input('length :'))
    area = width * length
    print(area)
elif (choice == 2) :
    width = int(input('width :'))
    length = int(input('length :'))
    area = width * length * 1/2
    print(area)
else :
    r = int(input('radius :'))
    area = r*r*3.14
    print(area)

