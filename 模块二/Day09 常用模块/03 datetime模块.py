import datetime

# datetime.time 处理时分秒
# datetime.date # 处理年月日
# datetime.datetime # 处理年月日 时分秒
# datetime.timedelta # 处理时间差

# datetime.datetime

# （1） 创建日期对象
# 获取当前日期对象
# now = datetime.datetime.now()
# print(now, type(now))
# today = datetime.datetime.today()
# print(today, type(today))
# # 获取任意时间对象
# date = datetime.datetime(2025, 12, 25, 12, 25, 25)
# print(date, type(date))
# (2) datetime 对象的属性 对象.变量名
# now = datetime.datetime.now()
# print(now.year, type(now.year))
# print(now.month, type(now.month))
# print(now.day, type(now.day))
# print(now.hour, type(now.hour))
# print(now.minute, type(now.minute))
# print(now.second, type(now.second))

# （3）datetime 对象格式化字符串转换
# now = datetime.datetime.now()
# s = now.strftime("%d/%m/%Y, %H:%M:%S")
# print(s, type(s))

# (4) 将字符串转换成时间对象
# time_str = "2020 12 20 10:0:0"
# my_time = datetime.datetime.strptime(time_str, "%Y %m %d %H:%M:%S")
# print(my_time, type(my_time))
