# gf = {"name": "高圆圆", "age": 23}

# 无序 属于容器类型
# print(len(gf))

# 增或改 字典对象[key]=值
# gf["age"] = 27
# print(gf)
# gf["height"] = 175
# print(gf)


# (2)删除
# del gf["age"]
# print(gf)

# (3) 查看键值
# print(gf["name"])  # 键不存在 报错

# (4) 成员判断 in
# print("names" in gf)
# print("age" in gf)


# （5） 遍历所有的键值对

gf = {"name": "高圆圆", "age": 23, "height": 175}

for key in gf:
    print(key, end=":")
    print(gf[key])
