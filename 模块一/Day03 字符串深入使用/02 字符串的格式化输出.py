# (1) 百分号%占位符

# name = "shanks"
# age = 18
# height = 185.152145
# s = """
#  员工信息:
#  姓名: %s
#  年龄: %s
#  身高: %s
# """ % (
#     name,
#     age,
#     height,
# )
# print(s)
# (2) f-str width 宽度 字符串左对齐 整数右对齐  宽度: 精度. :. 对齐方式 < > ^ *填充
# s = f"姓名: {name:15}, 年龄: {age:<5}, 身高: {height:>4.5}"
# print(s)
# name = "shanks2"
# age = 22
# height = 140.01501
# s = f"姓名: {name:15}, 年龄: {age:<5}, 身高: {height:>4.5}"
# print(s)
# 拓展

name = "shanks"
age = 18
height = 185.152145
s = f"""
 员工信息:
 姓名: {name}
 年龄: {age}
 虚岁：{age + 1}
 身高: {height}
 其他: {type(1 + 1 > 2)}
"""
print(s)
