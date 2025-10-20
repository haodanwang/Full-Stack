import datetime

# datetime模块下的date类
# 创建日期对象
# today = datetime.date.today()
# print(today, type(today))
# print(today.year)
# print(today.month)
# print(today.day)

# 创建指定日期
# my_date = datetime.date(2020, 12, 12)
# print(my_date, type(my_date))
#
# # (3) 将日期对象转换为格式化字符串
# ret = my_date.strftime("%d/%m/%Y")
# print(ret, type(ret))

# datetime.timedelta 时间间隔

# my_date01 = datetime.date(2020, 12, 12)
# my_date02 = datetime.date(2022, 1, 12)
# delta = my_date02 - my_date01
#
# print(delta.days)
# print(delta.total_seconds())
# print(type(delta))

# 案例2
# now = datetime.datetime.now()
# f_datetime = now + datetime.timedelta(days=7)
# print(f_datetime)
# print(type(f_datetime))
