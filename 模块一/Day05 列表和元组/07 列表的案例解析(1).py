# 1
# result_list = []
# for i in range(1, 11):
#     result_list.append(i * i)
#
# print(result_list)

# 2 扑克牌
import random

poke_type = ["♥️", "♦️", "♠️", "♣️"]
poke_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
poke_list = []
for type in poke_type:
    for num in poke_num:
        poke_list.append(f"{type}{num}")
print(poke_list)

# (1)抽王八
# ret1 = random.choice(poke_list)
# ret2 = random.choice(poke_list)
# ret3 = random.choice(poke_list)
# print(ret1)
# print(ret2)
# print(ret3)
# (2) 炸金花
# ret1 = random.sample(poke_list, 3)
# for i in ret1:
#     poke_list.remove(i)
# ret2 = random.sample(poke_list, 3)
# for i in ret2:
#     poke_list.remove(i)
# ret3 = random.sample(poke_list, 3)
# print(ret1)
# print(ret2)
# print(ret3)
