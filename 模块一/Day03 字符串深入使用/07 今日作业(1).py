# 1
# s = "hello world"
# print(s[6:])
# print(s[-5:])
# print(s[-1:-6:-1])

# 2
# s = input("请输入的Y/y N/n:")
# s = s.lower()
# if s == "y":
#     print(True)
# elif s == "n":
#     print(False)
# else:
#     print("非法输入")

# 3

# 4
# name = input("请输入姓名:")
# names = "yuan rain eric alvin"
# print(name in names)

# 5
# s1 = input("请输入一个加法:")
# num = s1.split("+")
# print(num)
# print((int(num[0])) + (int(num[1])))

# 6
# phone = input("请输入手机号:")
# phone = phone[:4] + "****" + phone[-3:]
# print(phone)
# num = int(input("请输入一个三位数"))
# print(num // 100)
# print(num % 100 // 10)
# print(num % 10)
# print(num // 100 + num % 100 // 10 + num % 10)

# s = "level"
# print(s == s[::-1])

# ret = input("请输入一个字符串:")
# num = len(ret) % 4
# print(ret + "*" * (4 - num))
# phone = input("请输入手机号")
#
# print(
#     len(phone) == 11
#     and phone.isdigit()
#     and (phone.startswith("133") or phone.startswith("153"))
# )

# mail = input("请输入一个邮箱")
# mail1 = mail.split("@")
# print(mail1[0])
# print(mail1[1].split(".")[0])
