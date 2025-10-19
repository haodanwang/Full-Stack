import openpyxl

# 读取excel文件

# workbook = openpyxl.load_workbook("example.xlsx")
# sheet = workbook["Sheet1"]
#
# # 获取单元格数据
# value = sheet["A1"].value
# print(value)
#
# value2 = sheet["B2"].value
# print(value2)
#
# # 修改excel文件的内容
# sheet["B7"].value = "这是一个测试"
#
# # 保存后修改的excel文件
# workbook.save("example.xlsx")


# 创建一个Excel
workbook = openpyxl.Workbook()
sheet = workbook.active
# 写入数据到单元格
# sheet["A1"] = "hello"
# sheet["B1"] = "world"
# 写入一行数据
# sheet.append([1, 2, 3, 4, 5, 6, 7])
for i in range(1, 101):
    sheet.append([i, i**2, i**3, i**4])
workbook.save("newexample.xlsx")
