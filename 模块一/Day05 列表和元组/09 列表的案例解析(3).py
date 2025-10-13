shopping_cart = []

while 1:
    print("----购物车清单----")
    print("1.添加商品")
    print("2.删除商品")
    print("3.查看购物车")

    choice = input("请输入选项:")
    if choice == "1":
        item = input("请输入添加的商品名称:")
        shopping_cart.append(item)
        print(f"已添加商品:{item}")
        print("\n")
    elif choice == "2":
        item = input("请输入删除商品的名称:")
        if item in shopping_cart:
            shopping_cart.remove(item)
            print(f"已删除商品:{item}")
        else:
            print("该商品不存在")
    elif choice == "3":
        if len(shopping_cart) == 0:
            print("购物车为空！")
        else:
            print("*" * 20)
            for item in shopping_cart:
                print(f"目前购物车商品有:{item}")
    else:
        print("无效输入:")
