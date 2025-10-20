import json

# user = {"name": "汪", "email": "123@qq.com", "gender": "male"}
# print(json.dumps(user, ensure_ascii=False))  # 中文汉字不需要Unicode编码


#  案例2
# data = {
#     1000: "apple",
#     2000: "banana",
#     3000: "peache",
# }
# with open("data.json", "w") as f:
#     json.dump(data, f)

# with open("data.json", mode="r") as f:
#     data = json.load(f)
#     print(data)
#
# data = {int(k): v for k, v in data.items()}
# print(data)


# 案例3
# user = {"name": "汪", "email": "123@qq.com", "gender": "male"}
#
# # 有两个空格 一个是键值的 一个是分隔符:
# print(repr(json.dumps(user, ensure_ascii=False)))
#
# # 和JS解析出来的是一致的
# print(repr(json.dumps(user, ensure_ascii=False, separators=(",", ":"))))
#
# print(len(repr(json.dumps(user, ensure_ascii=False))))
# print(len(repr(json.dumps(user, ensure_ascii=False, separators=(",", ":")))))
