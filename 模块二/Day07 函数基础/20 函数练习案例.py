# data = input("请输入一段文本:")
#
#
# def cal_num():
#     count = 0
#     for char in data:
#         if char.lower() in "aeiou":
#             count += 1
#     return count
#
#
# print("元音字母出现的次数", cal_num())


# def cal_year(base, back, rate=0.0325):
#     total = base
#     year = 0
#     while total < back:
#         total = total + total * rate
#         year += 1
#     return year
#
#
# print(cal_year(20000, 200000))
# def get_fib(num):
#     pre = 0
#     current = 1
#     next = 1
#     for _ in range(num):
#         next = pre + current
#         pre = current
#         current = next
#
#     return next
#
#
# print(get_fib(11))
