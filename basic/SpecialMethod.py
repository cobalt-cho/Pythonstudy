'''
special method 사용하기
'''

class Circle :
    def __init__(self,radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius ==other.radius

# __eq__() 사용시 ==를 이용

c1 = Circle(10)
c2 = Circle(20)

if c1 ==c2 :
    print("반지름은 동일하다")

class Vector2D :
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y+other.y

    def __sub__(self, other):
        return self.x - other.x, self.y-other.y

    def __str__(self):
        return '%d,%d'%(self.x,self.y)

u = Vector2D(0,1)
v = Vector2D(1,1)
a = u+v
print(a)

