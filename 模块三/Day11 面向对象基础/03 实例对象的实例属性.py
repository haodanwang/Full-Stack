# 声明类
class Dog:
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    # 类方法
    def bark(self):
        print("狗狂吠")

    def bite(self):
        print("狗咬人")

    def fetch(self):
        print("狗捡球")


# 创建类对象的过程：类的实例化

alex = Dog()
Peiqi = Dog()

# 实例对象属性赋值   实例对象.属性=值 向实例空间写属性和值

alex.name = "Alex"
alex.age = 10

Peiqi.name = "武大郎"
Peiqi.age = 8
print(alex.name)
print(Peiqi.name)
alex.age = 30
print(alex.age)

# (2)
# alex.bark()
alex.bark = 1000
# print(alex.__dict__)
# print(Peiqi.__dict__)
alex.legs_num = 5
print(alex.legs_num)
