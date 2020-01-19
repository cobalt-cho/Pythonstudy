class Animal :
    def __init__(self,name):
        self.name = name

    def speak(self):
        return '알 수없음'

class Dog(Animal):
    def speak(self):
        return '멍멍'

class Cat(Animal):
    def speak(self):
        return '야옹'

aList = [Dog('d1'),Dog('d2'),Cat('c1')]

for animal in aList :
    print(animal.name + animal.speak())