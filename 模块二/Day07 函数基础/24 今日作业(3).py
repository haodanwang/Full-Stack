# # 12
# def a():
#     print("aaa")
#
#
# def b():
#     print("bbb")
#
#
# def c():
#     print("ccc")
#
#
# def d():
#     print("ddd")
#
#
# def e():
#     print("eee")
#
#
# func_list = [a, b, c, d, e]
# func_list[2]()
#
# func_dict = {"a": a, "b": b, "c": c, "d": d, "e": e}
# func_dict["d"]()
import sys

shopping_cart = []


def add_to_cart():
    name = input("请输入需要添加商品的名称:")
    price = int(input("请输入商品的价格:"))
    num = int(input("请输入商品的数量:"))
    new_item = {"name": name, "price": price, "quantity": num}
    shopping_cart.append(new_item)
    print(f"{name}已经添加到购物车,数量为{num}")
    print(f"当前购物车商品为:{shopping_cart}")


def remove_to_cart():
    num = int(input("请输入删除商品的序号:"))
    index = num - 1
    del_goods = shopping_cart.pop(index)
    print(f"{del_goods.get('name')}删除成功")


def show_to_cart():
    total = 0
    for i, u in enumerate(shopping_cart, 1):
        print(
            f"当前购物车有:{i}.{u.get('name')},数量为:{u.get('quantity')},该商品总价为:{(u.get('quantity') * (u.get('price')))}"
        )
        total += u.get("price") * u.get("quantity")
    print(f"商品总价为：{total}")


def exit_pro():
    print("感谢购物车")
    sys.exit()


while 1:
    print(
        """
       1.添加商品到购物车
       2.删除商品
       3.查看购物车以价格
       4.退出
    """
    )
    choice = input("请输入选项:")
    handle = {"1": add_to_cart, "2": remove_to_cart, "3": show_to_cart, "4": exit_pro}
    func = handle.get(choice)
    if func:
        func()
    else:
        print("无效输入")
