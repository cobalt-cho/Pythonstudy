class Vehicle :
    def __init__(self,name):
        self.name = name

    def drive(self):
        raise NotImplementedError(" 추상 메소드 ")

    def stop(self):
        raise NotImplementedError(" 추상 메소드 ")


class Car(Vehicle):
    def drive(self): # 오버라이딩
        return "승용차 운전"

    def stop(self): # 오버라이딩
        return "승용차 정지"


class Truck(Vehicle):
    def drive(self):
        return "트럭 운전" # 오버라이딩
    def stop(self):
        return "트럭 정지" # 오버라이딩

cars = [Truck('t1'),Truck('t2'),Car('c1')]

for car in cars:
    print(car.name + car.drive())