# 使用切片操作符 进行拷贝
# l1 = [1, 2, 3, 4, 5]
# l2 = l1[:]
# print(id(l1))
# print(id(l2))
# print(l1)
# print(l2)
# l2[0] = 2
# print(l1)
# print(l2)
# print(id(l1[0]))
# print(id(l1[1]))
# print(id(l1[2]))
# print(id(l2[0]))
# print(id(l2[1]))
# print(id(l2[2]))

# 案例2
# l1 = [1, 2, 3, [4, 5]]
# l2 = l1[:]
# l1[3][0] = 2
# print(l1)
# print(l2)
# 深拷贝
import copy

l1 = [1, 2, 3, [4, 5]]
l2 = copy.deepcopy(l1)
