# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    # 类方法
    def bark(self):
        print(f"{self.name}正在狂吠")

    def bite(self, person):
        print(f"{self.name}咬{person}")

    def fetch(self):
        print(f"{self.name}在捡球")

    def show_info(self):
        print(f"{self.name, self.age, self.breed, self.color}")


# 创建类对象的过程：类的实例化

alex = Dog()
Peiqi = Dog()

# (1) self
# print(alex)
# alex.bark()
# alex.bite("shanks")


# (2)
alex.name = "Alex"
alex.breed = "斗牛犬"
alex.color = "浅灰色"
alex.age = 5
alex.bark()
alex.bite("shanks")
alex.fetch()
alex.show_info()
# Peiqi.name = "武大郎"
# Peiqi.bark()
