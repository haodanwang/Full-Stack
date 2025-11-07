# s = str("hello world")
# print(id(s), type(s))
# s.upper()
class Dog(object):
    # 类属性
    legs_num = 4
    has_hair = True
    has_tail = True

    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age


alex = Dog("alex", "斗牛犬", "黄色", 5)


# print(type(alex))
# print(alex)
# alex.age = 10
# print(alex.age)


# 自定义类型对象为可变数据类型


# def foo(x):
#     print(x)
#     print(type(x))


# def bar(y):
#     print(y)
#     y.age = 10
#
#
# bar(alex)
# print(alex.age)


def Test01():
    peiQI = Dog("Peiq", "斗狗犬", "绿色", 10)
    return peiQI


pq = Test01()
print(pq.name)
