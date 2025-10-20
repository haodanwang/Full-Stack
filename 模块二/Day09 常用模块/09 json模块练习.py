# 持久化数据
import json

# 序列化
with open("data.json", mode="w") as f:
    d = {"name": "shanks", "age": 18, "is_married": False, "gf": None}
    # data_json = json.dumps(d)
    # f.write(data_json)
    json.dump(d, f)  # 方式2

with open("data.json", mode="r") as f:
    # data_json = f.read()
    # d = json.loads(data_json)
    d = json.load(f)
    print(d, type(d))
