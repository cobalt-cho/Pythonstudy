class Person :
    def __init__(self,name,number):
        self.name = name
        self.number = number # 주민등록번호

    def __str__(self):
        return "%s,%d"%(self.name,self.number)

class Student(Person):
    def __init__(self,name,number,classes,gpa):
        super().__init__(name,number)
        self.classes = []
        self.gpa = gpa

    def enrollCourse(self,course):
        self.classes.append(course)

class Tearcher(Person):
    def __init__(self,name,number,courses,salary):
        super.__init__(name,number)
        self.courses = []
        self.salary = salary

    def assignTeaching(self,course):
        self.courses.append(course)


