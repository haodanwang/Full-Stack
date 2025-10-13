# for i in range(1, 10):
#     if i == 8:
#         continue
#     print(i)

result = 0
for i in range(1, 101):
    if i % 13 != 0:
        continue
    result += i

print(result)
