peiQi_hobby = {"螺蛳粉", "臭豆腐", "榴莲", "apple"}

alex_hobby = {"螺丝粉", "臭豆腐", "榴莲", "屎", "pizza"}

shanks_hobby = {"pizza", "salad", "ice cream", "臭豆腐", "榴莲"}

hobbies = [peiQi_hobby, shanks_hobby, alex_hobby]

# 给佩奇推荐
hobbies.remove(peiQi_hobby)
# peiQi_list = []
peiqi_set = set()
for hobby in hobbies:
    if len(peiQi_hobby.intersection(hobby)) >= 2:
        peiqi_set.update(hobby - peiQi_hobby)

# print(list(set(peiQi_list)))
# 版本1 类型转换

print(peiqi_set)
