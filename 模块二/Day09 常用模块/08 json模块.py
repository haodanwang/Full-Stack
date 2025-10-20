import json

# 序列号 将本语言支持的高级数据类型对象转换为json格式字符串的过程

# num = 3.14
# name = "shanks"
# l = [1, 2, 3]
# t = (4, 5, 6)
# d = {"name": "shanks", "age": 18, "is_married": False, "gf": None}
#
# print(repr(json.dumps(num)))  # 3.14
# print(repr(json.dumps(name)))  # "shanks"
# print(repr(json.dumps(l)))  # [1, 2, 3]
# print(repr(json.dumps(t)))  # [4, 5, 6]
# print(
#     repr(json.dumps(d))
# )  # {"name": "shanks", "age": 18, "is_married": false, "gf": null}

# d = {"name": "shanks", "age": 18, "is_married": False, "gf": None}
# json_d = json.dumps(d)
# print(json_d)
#
# print(json.loads(json_d))

# 能否反序列化的前提 一定要是JSON格式的字符串
# s = '{"name":"yuan","age":18,"isMarried":false}'
# data = json.loads(s)
# print(data)
# s2 = '[{"name":"yuan","age":18,"isMarried":false},{"name":"rain","age":22,"isMarried":false}]'
# data = json.loads(s2)
# print(data, type(data))
# print(data[1]["name"])
