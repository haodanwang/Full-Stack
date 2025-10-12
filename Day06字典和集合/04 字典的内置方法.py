gf = {"name": "高圆圆", "age": 23}

# （1） 增或改 字典对象.update(字典对象)

# gf.update({"age": 27})
# print(gf)
# gf.update({"height": 175})
# print(gf)
# tmp = {"age": 27, "height": 175}
# gf.update(tmp)
# print(gf)

# （2） 删除键值对
# ret = gf.pop("age")
# print(ret)
# print(gf)

# 查看键值 get()
# name = gf.get("name")
# age = gf.get("ages")
# print(name)
# print(age)
name = gf.get("names", "匿名用户")
print(name)
