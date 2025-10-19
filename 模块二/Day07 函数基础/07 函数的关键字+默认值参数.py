def show_info(name, age, height=None, weight=None):
    print("*" * 20)
    print(f"【姓名{name}】")
    print(f"【年龄{age}】")
    if height:
        print(f"【身高{height}】")
    if weight:
        print(f"【体重{weight}】")


# show_info(name="shanks", age=12)
show_info("shanks", 12, weight=70)
