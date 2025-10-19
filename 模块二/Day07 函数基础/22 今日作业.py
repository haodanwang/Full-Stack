# 1
# def cal_cicle(r):
#     pai = 3.14
#     print(f"圆的周长为{2 * pai * r}")
#     print(f"圆的面积为{pai * r * r}")
#
#
# cal_cicle(2)
# 2
# def cal_BMI(height, weight):
#     bmi = weight / (height * 2)
#
#     if bmi < 18.5:
#         advice = f"您的BMI为{bmi},体重过轻,建议增加营养摄入"
#     elif 18.5 <= bmi < 24:
#         advice = f"您的BMI为{bmi},体重正常,请保持健康的生活方式"
#     elif 24 <= bmi < 28:
#         advice = f"您的BMI为{bmi},体重过重,建议适量控制饮食并增加运动"
#     else:
#         advice = f"您的BMI为{bmi},体重肥胖,建议减少高热量食物摄入并增加运动量"
#
#     print(advice)
#
#
# height = float(input("请输入您的身高:(单位:米)"))
# weight = float(input("请输入您的体重:(单位:千克)"))
# cal_BMI(height, weight)
import random
import string

# 3
# def random_code(s):
#     code = ""
#     for _ in range(s):
#         code += random.choice(string.ascii_letters + string.digits)
#     return code
#
#
# print(random_code(6))


# 4
# def cal_avg(a):
#     print(sum(a))
#
#
# cal_avg([1, 2, 3])
import math

# 5
# def cal(a):
#     if a == 0:
#         return 1
#     else:
#         return a * math.factorial(a - 1)
#
#
# print(cal(4))


# 6
# def foo(x):
#     x = x.copy()
#     x[0] = 100
#     x.append(4)
#     print(x)
#
#
# l = [1, 2, 3]
# foo(l)
# print(l)

# 7
# x = 10
#
#
# def my_func():
#     print(x)
#
#
# def outer():
#     x = 20
#     my_func()
#
#
# outer()
