# 函数版本

# 函数声明
"""
def 函数名():
    函数体
"""


def print_pokes():
    poke_type = ["??", "??", "??", "??"]
    poke_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    poke_list = []
    for type in poke_type:
        for num in poke_num:
            poke_list.append(f"{type}{num}")
    print(poke_list)


# 函数调用 一次声明 多次调用
print_pokes()
print("somethings")
print_pokes()
