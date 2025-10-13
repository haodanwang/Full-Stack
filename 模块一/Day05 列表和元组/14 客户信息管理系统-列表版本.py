# 初始化列表数据
customers = [
    ["Alice", 25, "alice@example.com"],
    ["Bob", 30, "Bob@example.com"],
    ["Charlie", 35, "charlie@example.com"],
]

# # (1) 添加客户
# name = input("请输入添加客户的姓名:")
# age = input("请输入添加客户的年龄:")
# email = input("请输入客户的邮箱:（@example.com结尾）") + "@example.com"
# customers.append([name, age, email])
# print(f"添加客户{name}成功！")
# print(f"当前客户有{customers}")
#
# # (2) 删除客户
# del_customer_name = input("请输入删除客户的姓名:")
# for name in customers:
#     if name[0] == del_customer_name:
#         customers.remove(name)
#         print(f"客户{name[0]}已经被删除")
#         break
# else:
#     print("没有该客户")
# print(f"当前客户还剩下{customers}")

# update_customer = input("请输入要更新的客户信息:")
# name = input("请输入更新后的用户姓名:")
# age = input("请输入更新后的年龄:")
# email = input("请输入客户的邮箱:（@example.com结尾）") + "@example.com"
#
# for customer in customers:
#     if customer[0] == update_customer:
#         customer[0] = name
#         customer[1] = age
#         customer[2] = email
#         print("客户信息修改成功")
#         break
# else:
#     print("没有该客户的信息")
#
# print(f"当前客户列表为{customers}")

# （3）查看某一位客户信息
# query_customer_name = input("请输入查看客户的姓名:")
# for customer in customers:
#     if customer[0] == query_customer_name:
#         print(f"姓名:{customer[0]},年龄:{customer[1]},邮箱:{customer[2]}")
#         break
# else:
#     print("没有该客户信息")

# 遍历每一个客户
for customer in customers:
    print(f"姓名:{customer[0]:10},年龄:{customer[1]},邮箱:{customer[2]}")
