class Car(object):
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")


car1 = Car("Toyota", "Camry")
# car2 = Car("honda", "Accocrd")
# print(Car.total_cars)

# 通过类对象调用实例方法
Car.accelerate(car1)
