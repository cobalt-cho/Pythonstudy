class Vehicle :
    def __init__(self,name):
        self.name = name

    def drive(self):
        raise NotImplemented("abstract method")

    def stop(self):
        raise NotImplemented("abstract method")

class Car(Vehicle):
    def drive(self):
        return "승용차 운전"
    def stop(self):
        return "승용차 정지"

class Truck(Vehicle):
    def drive(self):
        return "트럭 운전"
    def stop(self):
        return "트럭 정지"

cars = [Truck('t1'),Truck('t2'),Car('c1')]

for car in cars :
    print(car.name, ":",car.drive())
