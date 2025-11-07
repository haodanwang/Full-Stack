# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        print("init执行")
        print(id(self))
        print(f"{self.name, self.age, self.breed, self.color}")

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

# alex = Dog()
# alex.init_pro("alex", "斗牛犬", "黄色", 5)
# alex.show_info()

# (1) self
# print(alex)
# alex.bark()
# alex.bite("shanks")


# (2)

# alex.bark()
# alex.bite("shanks")
# alex.fetch()
# alex.show_info()
# # Peiqi.name = "武大郎"
# # Peiqi.bark()
alex = Dog("alex", "斗牛犬", "黄色", 5)
print("alex::", id(alex))
