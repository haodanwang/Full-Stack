num1 = int(input("请输入一个数字"))
num2 = int(input("请输入一个数字"))

if num1 < num2:
    num1, num2 = num2, num1

print(f"{num2}为最小值")
