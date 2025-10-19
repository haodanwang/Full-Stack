# 返回的是一个文件的操作句柄
f = open("05 hello.txt", mode="r", encoding="UTF-8")
data = f.read()  # 读所有的字符
print(data)
