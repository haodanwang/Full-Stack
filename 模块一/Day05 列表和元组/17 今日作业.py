# 1
# number = [5, 2, 9, 1, 7, 6]
# number.sort()
# number.reverse()
# print(number)


# 2
# num = [1, 3, 5, 7, 9, 12, 15]
# ret = [i for i in num if i > 5]
# print(ret)

# 3
# l = [23, 4, 5, 66, 76, 12, 8, 23, 65]
# l = [i for i in l if i % 2 == 0]
# print(l)

# 4
# number = [1, 2, -3, 4, -5, 6, 7, -8, 9]
# result = 0
# for i in number:
#     if i > 0:
#         result += i
# print(result)

# 5
# l1 = ["shanks", "alex", "eric"]
# l2 = []
# for i in l1:
#     l2.append(i[::-1])
# print(l2)
# l1 = ["shanks", "alex", "eric"]
# l2 = [i[::-1] for i in l1]
# print(l2)

# 6
# number = [1, 2, 3, 2, 4, 3, 5, 6, 5]
# for i in number:
#     count = 0
#     for j in number:
#         if j == i:
#             count += 1
#     if count > 1:
#         number.pop(i)
# print(number)
# number = [1, 2, 3, 2, 4, 3, 5, 6, 5]
# l = []
# for i in number:
#     if i not in l:
#         l.append(i)
# print(l)

# 7
# number = [1, 7, 12, 9, 2, 12, 72, 45, 33]
# number.sort()
# print(number[0])
# number.reverse()
# print(number[0])
# number = [1, 7, 12, 9, 2, 12, 72, 45, 33]
# max = number[0]
# min = number[0]
# for i in number:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# print(max)
# print(min)
# 8
# number = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_list = []
# for i in number:
#     for j in i:
#         new_list.append(j)
#
# print(new_list)
# 嵌套循环推导式
# print([j for i in number for j in i])

# 9
# number = [1, 2, -3, 4, -5, 6, 7, -8, 9]
# result = 0
# count = 0
# for i in number:
#     if i > 0:
#         result += i
#         count += 1
#
# print(result / count)

# 10
# poke_type = ["♥️", "♦️", "♠️", "♣️"]
# poke_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# poke_list = []
# for type in poke_type:
#     for num in poke_num:
#         poke_list.append(f"{type}{num}")
#
# for _ in range(5):
#     ret = random.sample(poke_list, 3)
#     print(ret)
#     for i in ret:
#         poke_list.remove(i)

# 11
# number = [1, 700, 12, 9, 3, 12, 72, 45, 33, 701]
# number.sort()
# max = number[-1] - number[0]
# print(max)
# min_list = []
# result = 0
# for i in number:
#     for j in number:
#         if i > j:
#             result = i - j
#             min_list.append(result)
#         elif i < j:
#             result = j - i
#             min_list.append(result)
#         else:
#             continue
#
# # print(min_list)
# min_list.sort()
# min = min_list[0]
# print(min)

# 12
# number = [1, 700, 12, 9, 3, 12, 72, 45, 33, 701]
# result = 0
#
# result_big_avg = []
# result_avg = 0
# for i in number:
#     result += i
# avange = result / (len(number))
# print(avange)
#
# for j in number:
#     if j > avange:
#         result_big_avg.append(j)
#         result_avg += j
# print(result_big_avg)
# print(result_avg)

# 13
# score = [[85, 90, 78], [76, 82, 88], [90, 92, 86], [68, 72, 80], [92, 88, 90]]
# for i in score:
#     result = 0
#     for j in i:
#         result += j
#     print(f"学生{i}的{len(i)}科平均分为:{result / (len(i))}")
#
# chinses = 0
# Math = 0
# english = 0
# for i in score:
#     chinses += i[0]
#     Math += i[1]
#     english += i[2]
#
# print(f"{chinses}的平均分为:{chinses / (len(score))}")
# print(f"{Math}的平均分为:{Math / (len(score))}")
# print(f"{english}的平均分为:{english / (len(score))}")

#
# works = ["作品1", "作品2", "作品3", "作品4", "作品5", "作品6", "作品7", "作品8", "作品9", "作品10"]
# n = int(input("请输入需要查看的页数:"))
# ret = works[(n * 3 - 3) : (n * 3)]
# print(f"用户输入{n}获取到的作品为:{ret}")
