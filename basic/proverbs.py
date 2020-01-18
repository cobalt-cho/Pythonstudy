# 텍스트 파일을 읽어 몇 단어를 썼는지 확인하는 프로그램

# text에서 문자만 추출하고 소문자로 바꾼다
def process(w):
    output = ""
    for ch in w :
        if(ch.isalpha()): # 문자 추출
            output +=ch
    return output.lower() # 소문자로 변경

words = set() # 공백 세트 정의

fname = input("input file name")
file = open(fname,"r")

for line in file :
    linewords = line.split()
    for word in linewords:
        words.add(process(word))

print('사용된 단어의 개수 =', len(words))
print(words)

