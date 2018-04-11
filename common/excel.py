# coding=utf-8
import xlrd,xlwt

# 用来操作excel
class Excel():
    def __init__(self):
        pass

    def excelRead(self,path):
        wb=xlrd.open_workbook(path) #打开excel文件
        sh=wb.sheet_by_index(0) #通过sheet索引获取
        #sh1=wb.sheet_by_name(name) #通过sheet名称获取
        #nrows=sh.nrows #
        #col_data = sh.col_values(0) #获取第X列的值
        row_data = sh.row_values(4) #获取第X行的值
        print(row_data)
   # def excelwrite(self,path):

a=Excel()
a.excelRead("C:/Users/admin/Desktop/用户申购发票申请表 .xlsx")