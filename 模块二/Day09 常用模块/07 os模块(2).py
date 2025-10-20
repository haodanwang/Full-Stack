import os

# 一、 执行系统命令
# os.system("dir")
# ret = os.popen("dir")
# print(ret.read())


# 二、路径操作

# （1）os.path.join()
# print(os.path.join("a", "b", "c"))
# print(os.path.sep)
# # 将路径分割成目录和文件名
# print(os.path.split("E:\python\python.exe"))

# （3）os.path.basename() 返回文件名称 os.path.dirname 返回目录名称
# s = "E:\\python\\python.exe"
# print(os.path.basename(s))
# print(os.path.dirname(s))

# （4）判断路径是否存在
print(os.path.exists("E:\\python"))
