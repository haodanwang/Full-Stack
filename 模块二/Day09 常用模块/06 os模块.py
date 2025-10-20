import os

# 一、文件和目录操作
# （1）os.getpwd( ) 获取当前工作目录的路径
# print(os.getcwd())
# (2) os.chdir() 修改当前工作目录为指定路径
# os.chdir("../Day08 文件操作")
# print(os.getcwd())

# (3) os.listdir() 返回指定目录中的文件和目录列表
# print(os.listdir(os.getcwd()))
# (4)  os.mkdir() 创建一个新的目录
# os.mkdir("apple")
# (5) os.makedirs 递归创建文件夹
# os.makedirs("apple/banana/peache")
# （6）os.remove() 删除指定的文件
# os.remove("123.txt")

# (7)  os.removedirs() 递归删除目录 包括所有的子目录

# (8) os.rename() 将该文件或者目录从src重命名为dst
# os.rename("apple.txt", "banana.txt")
