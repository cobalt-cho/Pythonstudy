li = []

choice = 0

while(choice!=9):
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    print()
    choice = int(input("메뉴 선택"))
    print()
    if choice==1:
        print(li)
    elif choice==2 :
        name = input("이름을 입력하시오")
        li.append(name)
    elif choice == 3 :
        deleteName = input("삭제 할 이름을 입력하시오")
        if deleteName in li :
            li.remove(deleteName)
        else :
            print("등록된 이름이 아닙니다")
    elif choice == 4:
        changeName = input("변경하고 싶은 이름")
        if changeName in li :
            index = li.index(changeName)
            li[index] = input("변경 할 이름")
        else :
            print("등록 된 이름이 아님")
    elif choice == 9 :
        print("EXIT")
        break
    else :
        print("잘못된 메뉴 선택")
