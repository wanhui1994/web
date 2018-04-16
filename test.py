# coding=utf-8
import xlrd,pymysql,xlwt

class Mysql():
    # def excel(self,name,name1):
    #     wr=xlwt.Workbook(name)  #创建一个excel文件表
    #     sh=wr.add_sheet(name1)


    def mysql(self,ho,pr,us,pas,base,name):
        wr=xlwt.Workbook(name)  #创建一个excel文件表

        sh=wr.add_sheet('test1')
        db=pymysql.connect(host=ho,port=pr,user=us,password=pas,database=base)
        cu=db.cursor()
        sql="""SELECT * FROM `course` WHERE AGE=999"""
        cu.execute(sql)
        dis=cu.description #获取查询表的字段标题
        all=cu.fetchall()

        for i in range(int(len(dis))):  # 获取需要查询表的标题值
            sh.write(0,i,dis[i][0])       #写入的时候 0（第一行） i（列） dis（插入第几个元祖中的第一个数据）
            wr.save("C:/Users/admin/Desktop/"+name+'.xls') #保存表格

        for c in range(1,len(all)+1):  #由于第一行插入了标题，那么就是从第二行开始进行数据插入
            for col in range(0,len(dis)):  #
                sh.write(c,col,u'%s' % all[c-1][col])  # c(是第几行) col（第几列） c-1(由于我们是从第二行插入数据的所以+1，但是元素读取需要-1) col（第几个元素插入)
                wr.save("C:/Users/admin/Desktop/"+name+'.xls')
        cu.close()
        db.close()



        # result=cu.fetchall()
        # for i in range(len(result)):
        #     print(i)


aa=Mysql()
aa.mysql("192.168.10.215",3306,"root","123456","testlibrary","test")