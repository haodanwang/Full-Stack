# x = 1
#
# # LEGB原本那种 L>E>G>B
# """
# L → Local（局部作用域）
# E → Enclosing（嵌套作用域）
# G → Global（全局作用域）
# B → Built-in（内建作用域）
# """


# def foo():
#     x = 10
#     print("foo", x)
#
#
# foo()
# print("全局", x)

# x = 1
#
#
# def Test01():
#     x = 10
#
#     def Test02():
#         # x = 100
#         # print("test02的", x)
#         print(id)
#
#     Test02()
#     print("hello Test01")
#
#
# Test01()


# 案例3
# def Test(x, y):
#     print(x)
#     print(y)
#
#
# x = 1
# y = 2
# Test(x, y)


# 案例4
# def f00():
#     x = 10
#
#
# def bar():
#     y = 20
#     print(y)


# 案例5
# def print_pokes():
#     poke_type = ["♥️", "♦️", "♠️", "♣️"]
#     poke_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#     poke_list = []
#     for type in poke_type:
#         for num in poke_num:
#             poke_list.append(f"{type}{num}")
#     print(poke_list)
#
#
# print_pokes()


# 案例 2
# x = 1
#
#
# def set_x():
#     global x  # 全局变量声明
#     x = 100
#     print(id(x))
#     print("foo的x", x)
#
#
# set_x()
# print("全局的x", x)
# print(id(x))
x = 1


def foo():
    x = 100

    def bar():
        nonlocal x
        x = 1000

    print("bar的x", x)
    bar()


foo()
