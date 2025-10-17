# def add(x, y):
#     print(x + y)
#
#
# add(1, 2)


def add(name, *args):
    ret = 0
    for i in args:
        ret += i
    print(ret)
    print(name)


add("shanks", 2, 3, 4, 5)
