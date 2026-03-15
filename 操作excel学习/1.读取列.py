import openpyxl
from openpyxl import load_workbook
import pandas as pd
import paddlecor

# 加载Excel文件
# workbook = load_workbook(r"C:\Users\李克聪\Desktop\工作簿3.xlsx")
# worksheet = workbook.active
# all_s =worksheet.max_nrow
# print(workbook)
# df=pd.read_excel(r"C:\Users\李克聪\Desktop\工作簿3.xlsx")
# df.index.name = "xx"
# print(df.reset_index().set_index("产品属性"))
# ss= df.loc[30,"二级分类"]
# print(ss)

image_name = input('名称')
ocr = PaddleOCR()
data = ocr.get_ocr(f'{image_name}.png')
print(data)


