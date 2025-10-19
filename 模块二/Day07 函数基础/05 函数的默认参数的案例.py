# 案例3
def cal(start, end=None):
    if end == None:
        start, end = 1, start
    result = 0
    for i in range(start, end + 1):
        result += i
    print(result)


cal(88)
cal(2, 100)
