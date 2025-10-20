import time

# (1) time.time() :获取当前时间的时间戳
"""
1.时间字符串 "2020/12/12"
2.时间元组对象: (2024,2,13,.)
3.时间戳：
   1970 1 1 0:0:0 0 为起始时间 按秒算
    
"""
# print(time.time() / 3600 / 24 / 365)
# （2） time.sleep  让程序阻塞n秒钟
#
# print("start")
# time.sleep(10)
# print("end")

# (3) 获取时间元组对象time.localtime()

# print(time.localtime())
# print(time.localtime()[0])
# print(time.localtime()[1])
# print(time.localtime()[2])

# (4) 时间戳和时间元组对象的相互转换
# print(time.mktime(time.localtime()))
# print(time.gmtime(1760884943.0)) # 国标时间

# (5) 将元组对象转换为指定时间格式的时间字符串
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
