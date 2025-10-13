s1 = "wang is very handsome"
s2 = "rain"
s3 = "10"
print(type(s1))
print(type(s3))
print(s3 + "10")

new01 = '习主席再提中欧“之桥"'
print(new01)

# 字符串的定义除了 '' "" """ """ 三种方式
c1 = """
day1
day2
day3
day4
"""
print(c1)
# PEP8规范 一行不能超过128个字符
c2 = (
    "day1day1day1day1day1day1day1day1day1day1day1day1day1day1day1"
    "day1day1day1day1day1day1day1day1day1day1day1day1day1day1d"
    "ay1day1day1day1day1day1day1"
)
print(c2)
print(type(c2))
