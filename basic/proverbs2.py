# 파일에 저장된 단어가 몇 번 나오는지 계산

dic = dict()

fname = input("input file name")
file = open(fname,'r')

for line in file :
    lineWords = line.split()
    for word in lineWords :
        if word not in dic :
            dic[word] =1
        else :
            dic[word]+=1

print(dic)