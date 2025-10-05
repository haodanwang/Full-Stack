age = int(input("请输入年龄:"))
if age > 18:
    print("成人电影")
    choice = input(
        """请输入分类:
                  1.国产区
                  2.欧美区
                  3.日韩区
                 """
    )
    if choice == "1":
        ...
    elif choice == "2":
        ...
    elif choice == "3":
        ...
    else:
        print("输入有误")
    print("观影结束")
else:
    print("少儿电影")
    print("科幻类")
    print("冒险类电影")

print("程序结束")
