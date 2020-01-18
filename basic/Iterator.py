# iterator, generator 사용

class MyCounter(object):
    def __init__(self,low,high):
        self.current = low
        self.high = high

    # iterator 객체로서 자신을 반환
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high :
            raise StopIteration
        else :
            self.current+=1
            return self.current-1

c = MyCounter(1,10)
for i in c :
    print(i,end=' ')

'''
iterator는 클래스를 이용하여 생성
generator는 함수를 이용하여 생성
'''
print()
def MyCounterGen(low,high):
    while low <= high :
        yield low
        low +=1

for i in MyCounterGen(1,10):
    print(i,end=' ')
