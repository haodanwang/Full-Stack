# 高阶函数 以函数作为参数或者以函数作为返回值的函数
# 一等公民   函数 类 模块
# 如果某个东西是“一等公民”，那意味着你可以：
# 把它 赋值给变量；
# 把它 作为参数传给函数；
# 把它 作为函数的返回值；
# x = 1
# y = x
#
#
# def foo():
#     print("foo")
#
#
# def bar():
#     print("bar")
#
#
# def dec(f):
#     print("start")
#     f()
#     print("end")
#
#
# # dec(foo)
# dec(bar)

# filter
# l = [2, 3, 45, 67, 86, 21]

# print([i for i in l if i % 2 == 0])


# def get_even(item):
#     return item % 2 == 0
#     # if item % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#
#
# print(list(filter(get_even, l)))
# print(list(filter(lambda item: item % 2 == 0, l)))

# map 映射

# l = [1, 2, 3, 4, 5, 6]
# # print([i**2 for i in l])
#
#
# print(list(map(lambda item: item * item, l)))


# sorted #只能传列表
# l = [34, 5, 6, 12, 41]
# l.sort()
# print(l)

# 案例1
data01 = [("yuan", 18), ("alex", 45), ("peiqi", 32)]

# 方式1
# def my_order(item):
#     return item[1]
#
#
# print(list(sorted(data01, key=my_order)))


# print(sorted(data01, key=lambda item: item[1]))
# print(sorted(data01, key=lambda item: item[1], reverse=True))

data02 = [
    {"name": "shanks", "age": 21, "height": 187},
    {"name": "rain", "age": 22, "height": 167},
    {"name": "alex", "age": 32, "height": 197},
]

print(sorted(data02, key=lambda item: item.get("age")))
