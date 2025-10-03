from decimal import Decimal

x = 1
y = 2
print(1 + 2)

a = 3.14
b = 1.11
print(a + b)
print(a - b)
# ret = round(a - b)
# print(ret)
# print(round(a - b, 2))#四舍五入精度限制
c = Decimal("3.14")
d = Decimal("1.11")
print(c - d)
# type() 打印数据对象的类型名
print(type(c))
print(type(a))
print(type(x))
