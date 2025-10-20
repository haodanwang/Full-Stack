import random

# (1) 生成0-1的随机浮点型数字

# print(random.random())
# print(round(random.random(), 3))
# print(random.random() * 100)
# print(round(random.random() * 100))


# def flip_coin():
#     if random.random() >= 0.5:
#         return "heads"
#     else:
#         return "tails"
#
#
# print(flip_coin())

# random.randint 返回范围的整数

# print(random.randint(1, 100))

# 案例2 投骰子


# def roll_dice():
#     return random.randint(1, 6)
#
#
# print(roll_dice())

# random.choice 序列多选1
# print(random.choice([11, 22, 33, 44, 55]))


# def drwm_prize():
#     paters = ["Alice", "shansk", "bob"]
#     return random.choice(paters)
#
#
# print(drwm_prize())

# random.example 序列 多选多

# ret = random.sample(range(1, 34), 6)
# ret.append(random.randint(1, 16))
# print(ret)
