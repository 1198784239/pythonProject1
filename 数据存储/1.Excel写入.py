import openpyxl
import pandas as pd
import xlwt

#
# # 创建新的列表
# workbook = openpyxl.Workbook()
#
# #获取默认的工作表
# sheet = workbook.active
#
# #写入数据
# sheet['A1']='姓名'
# sheet['B1']='年龄'
#
# #添加一行数据
# sheet.append(['Alice',25])
#
# #保存
# workbook.save('examle.xls')

# __________________________________使用pandas库________________________
data = {'姓名':['Alice','Jok'],'年龄':['25','12']}
Data = pd.DataFrame(data)
print(Data)
Data.to_excel('panda.xlsx',index=False)

# -----------------使用xlwt和xlrd库----------------------
workbook = xlwt.Workbook()

sheet = workbook.add_sheet('sheet1')

#写入数据
sheet.write(0,0,'姓名')
sheet.write(0,1,'年龄')
sheet.write(1,0,'JOL')
sheet.write(1,1,'22')

#保存数据
workbook.save('lxml.xls')