# （4） strip 去除两端的空格或者换行符
# name = input("姓名:")
# print(name, len(name), name.strip(), len(name.strip()))

# print("\nshanks\n")
# print("\nshanks\n".strip())
# s = "####abcd#####"
# print(s.strip("#"))
# print(s.rstrip("#"))
# print(s.lstrip("#"))

# (5)isdigit 判断字符串是否为数字字符串 判断整型
# print("123".isdigit())
# print("123.45".isdigit())

# split和join split 返回列表 join返回字符串

# cities = "北京 哈尔滨 重庆 大连"
# ret = cities.split(" ")
# print(ret)
# print(len(ret))
# ret = ["北京", "哈尔滨", "重庆", "大连"]
# s1 = ",".join(ret)
# print(s1)


# replace 和count
# cities = "北京 哈尔滨 重庆 大连"
# print(cities.replace(" ", ","))

# count 计算字符串中某个子字符串出现的次数
s1 = "hello world"
print(s1.count("o"), type(s1.count("o")))
