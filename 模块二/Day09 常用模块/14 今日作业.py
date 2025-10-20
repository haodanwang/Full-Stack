# 1
import os.path
from datetime import datetime, timedelta
import datetime
import random

#
# now = datetime.datetime.now()
# print(now.microsecond)


# 2
# import random
#
#
# def send_money(money, num):
#     points = sorted(random.sample(range(1, 100), num - 1))
#     points = [0] + points + [100]
#     points = [points[i + 1] - points[i] for i in range(num)]
#     return points
#
#
# money = int(input("请输入红包总金额:"))
# num = int(input("请输入红包的个数:"))
# ret = send_money(100, 7)
# print(f"红包的列表为:{ret}")

# 3
# my_date = datetime.datetime(2000, 3, 1)
# my_date_string = datetime.datetime.strftime(my_date, "%Y/%m/%d")
# future = datetime.datetime.strftime(my_date + timedelta(days=100), "%Y/%m/%d")
# print(f"{my_date_string}是星期{my_date.weekday() + 1},100天后是{future}")

# 4
# path1 = "Users"
# path2 = "yuanhao"
# path3 = "python"
# my_path = os.path.join(path1, path2, path3)
# print(my_path)

# 5

# result = os.path.exists("H:\\全栈开发\\模块二\\Day09 常用模块")
# if result:
#     os.mkdir("apple")
#     os.chdir("./apple")
#     with open("test.txt", mode="w") as f:
#         f.write("banana")
# else:
#     print("该文件夹不存在")
# 6
