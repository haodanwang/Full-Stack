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

# (1)alex和Peiqi的内存地址不一样

print(id(alex))
print(id(Peiqi))

# (2)实例对象通过句点符号 调用类的属性和方法
print(alex.legs_num)
print(alex.has_tail)

# (3) 调用的类的属性一定是同一个地址
print(id(alex.legs_num))
print(id(Peiqi.legs_num))

print(id(alex.bark))
print(id(Peiqi.bark))
