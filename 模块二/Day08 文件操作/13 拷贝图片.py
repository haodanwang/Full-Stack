# 版本1
# with open("月饼.jpg", "rb") as f:
#     data = f.read()
#
#     with open("卡通2.jpg", "wb") as f_write:
#         f_write.write(data)

# 版本2
# with open("卡通3.jpg", "wb") as f_write:
#     with open("月饼.jpg", "rb") as f_read:
#         f_write.write(f_read.read())
