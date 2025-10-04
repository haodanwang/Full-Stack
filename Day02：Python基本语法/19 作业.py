# a = 1
# b = a  # b=1
# c = b  # c=1
# a, d = c + 1, b + 2  # a=2,d=3
# print(a, d)

# r = float(input("请输入圆的半径:"))
# print(3.14 * 2 * r)
# print(3.14 * r * r)

# print(bool("2<1"))
# count = 0
# a, b, c, d, e = 1, 2, 3, 4, 5
# count += a
# print(count)
# count += b
# print(count)
# count += c
# print(count)
# count += d
# print(count)
# count += e
# print(count)

# score = float(input("请输入你的分数:"))
# if 80 <= score <= 100:
#     print("在区间内")
# else:
#     print("不在区间内")
# num = float(input("请输入一个数字:"))
# print(num >= 100 and num % 13 == 0)

year = int(input("请输入一个年份:"))
print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
