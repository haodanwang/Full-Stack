# 1 计算1-100的累加和


# def cal():
#     ret = 0
#     for i in range(1, 101):
#         ret += i
#
#     print(ret)
#
#
# # 函数调用 函数调用完成后 函数执行过程中产生的变量全部销毁
# cal()


def cal(m, n):
    result = 0
    for i in range(m, n + 1):
        result += i
    print(result)


cal(1, 100)
