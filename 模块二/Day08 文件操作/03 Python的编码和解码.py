# （1） 字符串进行编码 得到新的数据类型 字节byte
# s = "王"
# ret = s.encode("GBK")  # 默认UTF-8
# print(ret)
# print(type(ret))
#
# # 将字节或者字节串解码
# # data = b"\xe7\x8e\x8b"
# data = b"\xcd\xf5"
# print(type(data))
# ret = data.decode("GBK")
# print(ret)

# 字节应用 磁盘存储 网络传输
data = b"0xbf"
ret = data.decode()
print(ret)
