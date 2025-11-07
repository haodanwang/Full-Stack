class Car(object):
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")


car1 = Car("Toyota", "Camry")
Car.total_cars = Car.total_cars + 1
# car2 = Car("honda", "Accocrd")
# 类对象 调用空间存储的属性和方法
car2 = Car("honda", "Accocrd")
Car.total_cars = Car.total_cars + 1

print(Car.total_cars)
