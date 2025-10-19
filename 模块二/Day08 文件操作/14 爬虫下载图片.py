import requests

res = requests.get(
    "https://cdn.pixabay.com/photo/2017/11/19/07/30/girl-2961959_960_720.jpg"
)

# print(res.content)

# 写文件
with open("美女.jpg", "wb") as f:
    f.write(res.content)
