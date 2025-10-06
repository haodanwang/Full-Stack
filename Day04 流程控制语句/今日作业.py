# 1
# char = input("请输入一个字符:")
#
# if char.upper() in ("AEIOU"):
#     print("是元音字母")
# else:
#     print("不是元音字母")

# 2
# str = input("请输入一串字符串")
# count = 0
# for i in str:
#     if i.upper() in ("AEIOU"):
#         count += 1
#
# print(count)

# 3
# result = 0
# for i in range(1, 101):
#     if i % 13 == 0:
#         continue
#     else:
#         result += i
# print(result)

# 4
# id_card = input("请输入一个正确的身份证号:")
# if len(id_card) == 18:
#     if int(id_card[-2]) % 2 == 0:
#         print("是女性")
#     else:
#         print("是男性")
# else:
#     print("请输入正确的18位身份证号")

# 5
# money = 10000
# year = 0
# while money <= 20000:
#     money *= 1.0325
#     year += 1
# print(year)

# 6
# count = 2
# i = 0
# j = 1
# while count < 20:
#     feb = i + j
#     if (i == 0) and (j == 1):
#         print(i, end=" ")
#         print(j, end=" ")
#     print(feb, end=" ")
#     i, j = j, feb
#     count += 1
# 7
# num = int(input("请输入一个大于1的自然数:"))
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1
#
# if count == 2:
#     print(f"{num}是素数")
# else:
#     print(f"{num}不是素数")


# for-else
# num = int(input("请输入一个大于1的整数:"))
# for i in range(2, num):
#     if num % i == 0:
#         print(f"{num}不是素数")
#         break
# else:
#     print(f"{num}是素数")
# 8
# import random
#
# chance = 3
# while chance > 0:
#     num = random.randint(1, 10)
#     guess = int(input("请输入一个数字(1-10):"))
#     chance -= 1
#     if guess == num:
#         print(f"恭喜你才对了,花费了{3 - chance}次机会")
#         break
#     elif guess < num:
#         print("您猜数字比结果小 请继续")
#     elif guess > num:
#         print("您猜数字比结果大 请继续")
#     if chance == 0:
#         print("很遗憾没用猜对")
#         break
# import random
#
# num = random.randint(1, 10)
# for i in range(3):
#     guess = int(input("请输入需要猜的数字:"))
#     if guess < num:
#         print("小于猜的数字")
#         print(f"还剩下{2 - i}次机会")
#     elif guess > num:
#         print("大于猜的数字")
#         print(f"还剩下{2 - i}次机会")
#     else:
#         print("恭喜你猜对了,数字为:", guess)
#         print(f"还剩下{2 - i}次机会")
#         break
#
# else:
#     print("很遗憾 机会用完了")


# 9

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(i + j, end=" ")
#     print("")

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}*{i}=", i * j, end=" ")
#     print("")
