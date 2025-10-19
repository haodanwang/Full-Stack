# 案例1
# 如同有默认参数 默认参数一定要放在位置参数后面
# def show_info(name, age, height, weight, gender="男"):
#     print("*" * 20)
#     print(f"【姓名{name}】")
#     print(f"【年龄{age}】")
#     print(f"【身高{height}】")
#     print(f"【体重{weight}】")
#     print(f"【性别{gender}】")
#
#
# show_info("shanks", "18", "175", "60")
# show_info("shanks", "18", "175", "60", "女")


# 案例2
# def cal_shopping_cart(shopping_cart, qa=0.8):
#     total = 0
#     for goods in shopping_cart:
#         total += goods["price"] * goods["quantity"]
#
#     total = round(total * qa, 2)
#     print(total)
#
#
# shopping_cart01 = [
#     {"name": "mac电脑", "price": 14999, "quantity": 1},
#     {"name": "iphone15", "price": 9980, "quantity": 1},
# ]
# shopping_cart02 = [
#     {"name": "mac电脑", "price": 14999, "quantity": 4},
#     {"name": "iphone15", "price": 9980, "quantity": 2},
# ]
# cal_shopping_cart(shopping_cart01, 0.7)
# cal_shopping_cart(shopping_cart02)


# 案例3
def cal(end, start=1):
    result = 0
    for i in range(start, end + 1):
        result += i
    print(result)


cal(88)
cal(100, 2)
