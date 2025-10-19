# 1 返回默认值
# ret = print("Hello yuan")
# print(ret)


# 返回多个值
# 默认返回元组类型


def log():
    name = "shanks"
    age = 18
    email = "123@qq.com"
    return [name, age, email]


ret = log()
print(ret)
