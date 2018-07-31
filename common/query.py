#coding=utf-8

from pyquery import PyQuery as pq

class Py():

     def code_href(self):
        # 获取电商子站点的href链接
        doc = pq(url='http://www.faxuan.net/',encoding="utf-8")
        ul = doc(".provincelist2") #定位元素div所在位置
        ul1= doc(".provincelist3")
        res1 = ul1('a').items()    #
        res = ul('a').items()
        b=[]
        for li in res:
            if li.attr("href") in "javascript:void(0);":
                 pass
            else:
               b.append(li.attr('href'))

        for li1 in res1:
            if li1.attr("href") in "javascript:void(0);":
                 pass
            else:
                b.append(li1.attr('href'))

        return b


