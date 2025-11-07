class Car(object):
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(id(self.__class__))
        self.__class__.total_cars += 1

    def accelerate(self):
        print(f"一辆{self.make}的{self.model}正在加速")

    @classmethod
    def show_total_car(cls):
        print(id(cls))
        print(f"当前的{cls.total_cars}正在加速")


car1 = Car("Toyota", "Camry")
# car2 = Car("honda", "Accocrd")
print(id(Car))
Car.show_total_car()
