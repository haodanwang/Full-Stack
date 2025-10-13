s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# 方式1：操作符
# print(s1 & s2)
# print(s1 - s2)
# print(s2 - s1)
# print(s1 | s2)
# 方式2: 内置方法
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1.union(s2))
