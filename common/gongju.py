# coding=utf-8
import pymysql
import xlwt,xlrd
class Mysql():
    def mysql(self,ho,pr,us,pas,base):
        db=pymysql.connect(host=ho,port=pr,user=us,password=pas,database=base)
        cu=db.cursor()
        sql="""SELECT * FROM `course` WHERE AGE=999"""
        cu.execute(sql)
        result=cu.fetchone() #查询的第一条结果输出
        result1=cu.fetchall()  #查询的所有结果输出
        a=cu.description()


    def excelRead(self,path,name):
        wb=xlrd.open_workbook(path) #打开excel文件
        sh=wb.sheet_by_index(0) #通过sheet索引获取
        sh1=wb.sheet_by_name(name) #通过sheet名称获取
        nrows=sh.nrows
        col_data = sh.col_values(0) #获取第X列的值
        row_data = sh.row_values(4) #获取第X行的值

    def excelwrite(self,name,name1,path):
        wr=xlwt.Workbook(name)  #创建一个excel文件表
        sh=wr.add_sheet(name1)  #创建一个工作表对象
        sh.write(0, 0, 'EnglishName')   # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
        wr.save(path+name+'.xls')

    def mysqlwrite(self):   #搜索的mysql数据导入到一个excel




a=Mysql()
a.mysql("192.168.10.215",3306,"root","123456","testlibrary")
