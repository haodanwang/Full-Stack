# 初始化列表数据
customers = {
    1001: {"name": "Alice", "age": 25, "email": "alice@example.com"},
    1002: {"name": "shanks", "age": 22, "email": "shanks@example.com"},
}

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
        key = int(input("请输入客户的id:"))
        if key in customers.keys():
            print("id已存在,请重新输入:")
        else:
            name = input("请输入添加客户的姓名:")
            age = input("请输入添加客户的年龄:")
            email = input("请输入客户的邮箱:（@example.com结尾）") + "@example.com"
            customerD = {"name": name, "age": age, "email": email}
            customers.update({key: customerD})
            print(f"添加客户{name}成功！")
            print(customers)
    elif choice == "2":
        # (2) 删除客户
        del_customer_name = input("请输入删除客户的姓名:")
        for i in customers:
            if customers[i]["name"] == del_customer_name:
                customers.pop(i)
                print(customers)
                break
        else:
            print("没有这个用户")

    elif choice == "3":
        # 更新客户信息
        update_customer = input("请输入要更新的客户信息:")
        name = input("请输入更新后的用户姓名:")
        age = input("请输入更新后的年龄:")
        email = input("请输入客户的邮箱:（@example.com结尾）") + "@example.com"

        for customer in customers:
            if customers[customer]["name"] == update_customer:
                customers.update({customer: {"name": name, "age": age, "email": email}})
                print("客户信息修改成功")
                print(customers)
                break
        else:
            print("没有该客户的信息")
    elif choice == "4":
        # （3）查看某一位客户信息
        query_customer_name = input("请输入查看客户的姓名:")
        for customer in customers:
            if customers[customer]["name"] == query_customer_name:
                print(
                    "姓名:",
                    customers[customer]["name"],
                    "年龄:",
                    customers[customer]["age"],
                    "邮箱:",
                    customers[customer]["email"],
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
                    f"姓名:{customers[customer]['name']:10},年龄:{customers[customer]['age']},邮箱:{customers[customer]['email']}"
                )

    elif choice == "6":
        flag = False
    else:
        print("请输入正确的数字:")
