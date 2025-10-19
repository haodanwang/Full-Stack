# 函数声明

# def声明 函数名（形参1，形参2，形参3，形参4）


# 调用函数（包括参数）
# 函数名(实参1，实参2，实参3....)


# def add(x, y):
#     print(x + y)
#
#
# add(1, 2)
# add(10, 20)


# def cal(start, end):
#     ret = 0
#     for i in range(start, end + 1):
#         ret += i
#
#     print(ret)
#
#
# cal(1, 100)


# 案例3 发送邮件
def send_email(recipient, subject, content):
    print("连接服务器")
    print(f"收件人邮箱{recipient}")
    print(f"主题{subject}")
    print(f"内容{content}")


r = "alex@qq.com"
s = "重要通知"
c = "您已被解雇"
send_email(r, s, c)
