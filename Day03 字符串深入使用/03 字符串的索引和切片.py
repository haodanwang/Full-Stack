s = "Hello shanks"

# 索引的语法 字符串对象[索引] 获取的一个字符
# print(s[6], type(s))
# print(s[0])
# print(s[-1])

# （2）切片的语法 字符串对象[开始索引:结束索引:step]
# print(s[0:4])
# print(s[6:])  # 缺省
# print(s[:])

print(s[::-1])  # 翻转 从右向左
print(s[3:0:-1])  # 步长是负数 从大到小
print(s[-2:-4:-1])
