# 1
# dict1 = {"A": 1, "B": 2, "C": 3, "D": 4}
# dict2 = {"B": 20, "D": 10, "E": 50}
#
# total = []
# for i in dict1.keys():
#     if i in dict2:
#         total.append(i)
#
# print(total)

# 2
# my_dict = {"A": 10, "B": 5, "C": 15, "D": 20}
#
# max = my_dict["A"]
# for i in my_dict.values():
#     if i > max:
#         max = i
#
# print(max)
# max = list(my_dict.values())
# max.sort()
# print(max[-1])

# 3
# my_dict = {"A": 10, "B": 5, "C": 15, "D": 20}
# result = 1
# for i in my_dict.values():
#     result *= i
# print(result)


# 4
# my_list = [1, 2, 3, 4, 1, 4, 5, 2, 1]
#
# my_dict = {}
# for i in my_list:
#     my_dict.update({i: my_list.count(i)})
#
# print(my_dict)

# 5
# dict1 = {"A": 1, "B": 2, "C": 3}
# dict2 = {"B": 10, "D": 20, "C": 30}
# dic3 = dict1
# for i in dict2.keys():
#     if i in dic3:
#         dic3.update({i: (dict2[i] + dic3[i])})
#     else:
#         dic3.update({i: dict2[i]})
#
# print(dic3)

# 6
# l = [1, 12, 1, 2, 2, 3, 15]
# s = set(l)
# l = list(s)
# l.sort()
# print(l)

# 7
# students = [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 76},
#     {"name": "Charlie", "score": 90},
#     {"name": "David", "score": 68},
#     {"name": "Eva", "score": 92},
# ]
# student_total_number = len(students)
# students_total_socre = 0
# max = students[0]["score"]
# min = students[0]["score"]
# for score in students:
#     students_total_socre += score["score"]
#     if score["score"] > max:
#         max = score["score"]
#     if score["score"] < min:
#         min = score["score"]
#
# print(f"学生总人数为:{student_total_number}")
# print(f"学生总成绩为:{students_total_socre}")
# print(f"学生平均成绩为:{round((students_total_socre / student_total_number), 2)}")
# print(f"学生成绩最高为:{max},学生成绩最低为:{min}")
# 8
# students = {
#     "Alice": {"math": 85, "english": 90, "history": 78},
#     "Bob": {"math": 76, "english": 82, "history": 88},
#     "Charlie": {"math": 90, "english": 92, "history": 86},
#     "David": {"math": 68, "english": 72, "history": 80},
#     "Eva": {"math": 92, "english": 88, "history": 90},
# }
#
# student_total_score = 0
# for student, score in students.items():
#     student_total_score = (
#         score.get("math") + score.get("english") + score.get("history")
#     )
#     print(f"{student}的总分为:{student_total_score}")
#     print(f"{student}的平均分为：{round((student_total_score / 3), 2)}")

# 9
# config = {
#     "数据库": {"主机": "localhost", "端口": 3306, "用户名:": "admin", "密码": "passwd"},
#     "服务器": {"IP地址": "192.168.0.1", "端口": "8080", "日志级别": "INFO"},
# }
#
# config.get("服务器").update({"端口": 8090, "日志级别": "DEBUG"})
# print(config)
# 10

# 11
shopping_cart = [
    {"name": "mac电脑", "price": 14999, "quantity": 1},
    {"name": "iphone15", "price": 9980, "quantity": 1},
]

flag = True
while flag:
    print(
        """
       1.添加商品
       2.删除商品
       3.查看购物车以价格
       4.退出
    """
    )
    choice = input("请输入选项:")
    if choice == "1":
        name = input("请输入需要添加商品的名称:")
        price = int(input("请输入商品的价格:"))
        num = int(input("请输入商品的数量:"))
        new_item = {"name": name, "price": price, "quantity": num}
        shopping_cart.append(new_item)
        print(f"{name}已经添加到购物车,数量为{num}")
        print(f"当前购物车商品为:{shopping_cart}")
    elif choice == "2":
        num = int(input("请输入删除商品的序号:"))
        index = num - 1
        del_goods = shopping_cart.pop(index)
        print(f"{del_goods.get('name')}删除成功")

        # name = input("请输入需要删除商品的名称:")
        # for u in shopping_cart:
        #     if u.get("name") == name:
        #         shopping_cart.remove(u)
        #         print(f"{name}已删除，当前购物车还有{shopping_cart}")
        #         break
        # else:
        #     print("该商品不存在!")
    elif choice == "3":
        total = 0
        for i, u in enumerate(shopping_cart, 1):
            print(
                f"当前购物车有:{i}.{u.get('name')},数量为:{u.get('quantity')},该商品总价为:{(u.get('quantity') * (u.get('price')))}"
            )
            total += u.get("price") * u.get("quantity")
        print(f"商品总价为：{total}")
    elif choice == "4":
        flag = False
    else:
        print("无效输入,请重新输入:")
