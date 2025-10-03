# print的返回值 空值
# ret = print("hello")
# print(ret, type(ret))
# 案例2 变量初始化赋值

# 去重 解耦
num1 = int(input("请输入num1:"))
num2 = int(input("请输入num2:"))
operator = input("请输入运算符:")
result = None
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("请输入正确的运算符")

print(result)
