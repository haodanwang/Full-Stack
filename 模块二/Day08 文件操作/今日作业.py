# 1
# 2
# with open("06 relex小诗", mode="r") as f:
#     ret = f.readlines()
#     for i in ret:
#         pass

# 3
# with open("Sourece.txt", mode="r") as f:
#     data = f.readlines()
#     for i in data:
#         if i.startswith("#"):
#             i = i.replace("# ", "").strip()
#             j = eval(i)
#             with open("Target.txt", mode="a") as f_write:
#                 f_write.write(i + ":" + str(j) + "\n")


# 4 多个with open 到with open

# 5
# with open("05 hello.txt", mode="r", encoding="UTF-8") as f:
#     data = f.readlines()
#     result = 0
#     for i in data:
#         result += i.count("hello")
#
#     print(result)
