# 初始化列表数据
customers = [
    {"name": "Alice", "age": 25, "email": "alice@example.com"},
]

flag = True

while flag:
    print(
        """
        1.添加客户
        2.删除客户
        3.修改客户
        4.查询一个客户
        5.查询所有客户
        6.退出
    """
    )

    choice = input("请输入您的选择:")
    if choice == "1":
        # (1) 添加客户
        name = input("请输入添加客户的姓名:")
        age = input("请输入添加客户的年龄:")
        email = input("请输入客户的邮箱:（@example.com结尾）") + "@example.com"
        customerD = {"name": name, "age": age, "email": email}
        customers.append(customerD)
        print(f"添加客户{name}成功！")
        print(customers)
    elif choice == "2":
        # (2) 删除客户
        del_customer_name = input("请输入删除客户的姓名:")
        for i in customers:
            if i.get("name") == del_customer_name:
                customers.remove(i)
                print(f"当前还剩下{customers}")
                break
        else:
            print("没有这个用户！")

    elif choice == "3":
        # 更新客户信息
        update_customer = input("请输入要更新的客户信息:")
        name = input("请输入更新后的用户姓名:")
        age = input("请输入更新后的年龄:")
        email = input("请输入客户的邮箱:（@example.com结尾）") + "@example.com"

        for customer in customers:
            if customer.get("name") == update_customer:
                customer.update({"name": name, "age": age, "email": email})
                print("客户信息修改成功")
                print(customers)
                break
        else:
            print("没有该客户的信息")
    elif choice == "4":
        # （3）查看某一位客户信息
        query_customer_name = input("请输入查看客户的姓名:")
        for customer in customers:
            if customer["name"] == query_customer_name:
                print(
                    "姓名:",
                    customer["name"],
                    "年龄:",
                    customer["age"],
                    "邮箱:",
                    customer["email"],
                )
                break
        else:
            print("没有该客户信息")
    elif choice == "5":
        # 遍历每一个客户
        if len(customers) == 0:
            print("当前没有客户信息!")
        else:
            for customer in customers:
                print(
                    f"姓名:{customer['name']:10},年龄:{customer['age']},邮箱:{customer['email']}"
                )

    elif choice == "6":
        flag = False
    else:
        print("请输入正确的数字:")
