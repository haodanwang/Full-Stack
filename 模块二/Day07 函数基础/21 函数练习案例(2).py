# #def recommand_hobby():
#     peiQi_hobby = {"螺蛳粉", "臭豆腐", "榴莲", "apple"}
#
#     alex_hobby = {"螺丝粉", "臭豆腐", "榴莲", "屎", "pizza"}
#
#     shanks_hobby = {"pizza", "salad", "ice cream", "臭豆腐", "榴莲"}
#
#     hobby_list = [peiQi_hobby, shanks_hobby, alex_hobby]
#
#     # 给佩奇推荐
#     hobby_list.remove(peiQi_hobby)
#     # peiQi_list = []
#     peiqi_set = set()
#     for hobby in hobby_list:
#         if len(peiQi_hobby.intersection(hobby)) >= 2:
#             peiqi_set.update(hobby - peiQi_hobby)
#
#     # print(list(set(peiQi_list)))
#     # 版本1 类型转换
#
#     print(peiqi_set)
# recommand_hobby()
def recommand_hobby(name):
    hobby_dict = {
        "peiQi": {"螺蛳粉", "臭豆腐", "榴莲", "apple"},
        "alex": {"螺丝粉", "臭豆腐", "榴莲", "屎", "pizza"},
        "shanks_hobby": {"pizza", "salad", "ice cream", "臭豆腐", "榴莲"},
    }
    # 给佩奇推荐
    current_base_hobby = hobby_dict.pop(name)
    recommand_set = set()
    for name, hobby in hobby_dict.items():
        if len(current_base_hobby.intersection(hobby)) >= 2:
            recommand_set.update(hobby - current_base_hobby)

    return recommand_set

    # print(list(set(peiQi_list)))
    # 版本1 类型转换


print(recommand_hobby("alex"))
