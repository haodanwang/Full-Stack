# f = open("09 hello2.txt", mode="w", encoding="UTF-8")
# f.write("hello 汪 \n")
# f.write("hello")

# () writelines() 传一个列表
# f.writelines(["aaa \n", "bbb \n"])
# line = open("06 relex小诗", mode="r", encoding="UTF-8")
# data = line.readlines()
# print(data)
# f.writelines(data)

# () mode=a 模式 追加到最后一行
f = open("09 hello2.txt", mode="a", encoding="UTF-8")
f.write("hello,banana\n")
f.write("hello,apple\n")
f.close()
