gf_name_list = ["高圆圆", "刘亦菲", "赵丽颖", "范冰冰", "李嘉欣"]

# 删除元素 pop remove clear

# (1) pop 按索引删 pop返回值给的删除的内容 当pop不传入索引的时候 默认删除最后一个元素
# ret = gf_name_list.pop(3)
# print(gf_name_list)
# print(ret)

# 2 按内容删除 remove
# gf_name_list.remove("范冰冰")
# print(gf_name_list)

# 3  clear 清空列表
gf_name_list.clear()
print(gf_name_list)
