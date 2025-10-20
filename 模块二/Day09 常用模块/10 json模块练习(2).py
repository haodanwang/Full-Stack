import json

# '{"user":"shanks","pwd":123}' js实现的序列化

s = '{"user":"shanks","pwd":123}'

# 反序列化

# data = json.loads(s)
# print(data, type(data))
#
# user = data.get("user")
# pwd = data.get("pwd")
# print(user, pwd)

user = {"name": "shanks", "email": "123@qq.com", "gender": "male"}
# 序列化
data = json.dumps(user)
print(data, type(data))

# 前端 反序列化
# res=JSON.parse(res)
# {name: 'shanks', email: '123@qq.com', gender: 'male'}
# res.name
# 'shanks'
# res.e
# undefined
# res.email
# '123@qq.com'
# res.gender
# 'male'
