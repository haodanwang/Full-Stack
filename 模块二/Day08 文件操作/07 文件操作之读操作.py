# 返回的是一个文件的操作句柄
f = open("06 relex小诗", mode="r", encoding="UTF-8")
# data = f.read()  # 读所有的字符
# print(data)  # 光标数据会变

# # 光标位置
# print(f.tell())
# f.seek(0)  # 移到第一行
# data = f.read()  # 读所有的字符
# print(data)
# （2） 读取指定数量的字符
# data01 = f.read(6)
# print(data01)
#
# data01 = f.read(6)
# print(data01)
# f.seek(267)
# data01 = f.read(16)
# print(data01)
# line01 = f.readline()
# print(line01)

# 读取所有行
# line02 = f.readlines()
# print(line02)
# for i in line02:
#     print(i, end="")

# 遍历文件
for line in f:
    if len(line) > 20:
        print(line, end="")
