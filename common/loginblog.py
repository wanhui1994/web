# coding=utf-8
# import xlwt
# i=0
# wr=xlwt.Workbook('test')  #创建一个excel文件表
# sh=wr.add_sheet('wh')  #创建一个工作表对象
# while i<100:
#     sh.write(i,0, 'wh1')   # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
#     i+=1
# wr.save(r'C:/Users/admin/Desktop/test.xls')
import requests
b=1
while b<1000:
    url="http://salegl.faxuan.net:83/saless/service/billService!doAddBillInvoiceInfo.do?address=%E5%8C%97%E4%BA%AC%E6%B5%8B%E8%AF%95&bankCode=NULL&bankName=%E5%8C%97%E4%BA%AC%E9%93%B6%E8%A1%8C&claimAdmin=&contactName=&email=ceshi%40faxuan.net&id=1000221&invoiceInfoDomainName=%E4%B8%87%E6%83%A0%E6%B5%8B%E8%AF%95%E5%8D%95%E4%BD%8D&invoiceType=0&mailAddress=&mobilePhone=13121322232&number=9999&operator=wanhui&price=999&subscribeId=1000149&taxpayersCode=2223332232323&telPhone=12306&titleType=4_0&total=999999"
    a = requests.get(url)
    print(a.text)
    b=b+1