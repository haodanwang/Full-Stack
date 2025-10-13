# 课程信息字典
courses = {
    "CS101": "计算机科学导论",
    "ENG201": "高级英语写作",
    "MATH301": "线性代数",
    "PHY401": "物理学原理",
    "HIS501": "世界历史概论",
}
# 学生字典:
students = {"1001": {"user": "shanks", "pwd": "123"}}
# 学生选课字典
student_courses = {}
is_login = False
students_id = None
while True:
    print("欢迎使用选课系统!")
    print("1.注册学生")
    print("2.登录")
    print("3.选课")
    print("4.退课")
    print("5.查看已选课程")
    print("6.退出系统")
    chioce = input("请输入您的选择:")
    if chioce == "1":
        userid = input("请输入学生的学号:")
        user = input("请输入学生的姓名:")
        pwd = input("请输入学生的密码:")
        students[userid] = {"user": user, "pwd": pwd}
        print(f"学生{user}注册成功!")
    elif chioce == "2":
        userid = input("请输入您的学号")
        if userid in students:
            pwd = input("请输入密码")
            if students[userid]["pwd"] == pwd:
                is_login = True
                print(f"恭喜您{students[userid]['user']}登录成功")
                students_id = userid
            else:
                print("密码错误!请重新输入")
        else:
            print(f"学号{userid}不存在请注册!")
    elif chioce == "3":
        if is_login:
            print(f"当前登录人:{students_id}")
            print("*" * 50)
            for key, value in courses.items():
                print(f"课程id:{key}:课程名称:{value}")
            print("*" * 50)
            curses_code = input("请输入选秀的课程id:")
            # 方式1
            # if students_id in student_courses:
            #     if curses_code in student_courses[students_id]:
            #         print("该课程已存在!请重新选择!")
            #     else:
            #         student_courses[students_id].append(curses_code)
            #         print(f"再次选修:{students_id}选修{curses_code}成功")
            # else:
            #     # student_courses[students_id] = [curses_code]
            #     student_courses.update({students_id: [curses_code]})
            #     print(f"选修初始化:{students_id}选修{curses_code}成功")
            # 方式2:
            if students_id not in student_courses:
                student_courses[students_id] = []
            if curses_code in student_courses[students_id]:
                print("该课程已存在!请重新选择!")
            else:
                student_courses[students_id].append(curses_code)
                print(f"选修:{students_id}选修{curses_code}成功")
            print(student_courses)

        else:
            print("您好 请先登录后再进行操作")
    elif chioce == "4":
        if not is_login:
            print("请先登录:")
        if students_id in student_courses:
            print("*" * 50)
            for key, value in student_courses.items():
                print(f"当前您已经选修:{key}:{value}")
            print("*" * 50)
            curses_code = input("请输入您需要退课的课程:")
            student_courses[students_id].remove(curses_code)
            print(f"{students_id}已经成功退订{curses_code}")
            print(f"当前还剩下{student_courses}")
        else:
            print("您未选修过任何课程!")
    elif chioce == "5":
        if not is_login:
            print("请先登录")
        else:
            if students_id not in student_courses:
                print("您未选修过任何课程:")
            else:
                for i in student_courses[students_id]:
                    print(f"{i}:{courses[i]}")

    elif chioce == "6":
        print("感谢您使用选课系统,欢迎下次再来!")
        break
    else:
        print("请您输入有效的选项!")
