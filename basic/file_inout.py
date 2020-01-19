infile = open("phones.txt","r",encoding='UTF8')
s = infile.read(10) # 10글자 읽기
s2 = infile.readline() # 한 줄 씩 읽기 -> 10글자 읽고 난 나머지를 읽음

while s2!="":
    print(s2)
    s2 = infile.readline()


# 파일 쓰기
outfile = open("phones.txt","w")
outfile.write("배고프다")
outfile.write("참고 집가야지") # 기존 내용을 지우고 새로 씀, 파일이 없으면 생성

