#coding=utf-8

from web.blog.fxshop.blog_login_page import Login_ds
import unittest
from web.blog.fxshop.blog_home_page import home_page,url
import time

class Person(unittest.TestCase):

    def setUp(self):
        '''初始化类，访问网站点击进入个人中心'''
        self.ds1=Login_ds()
        self.ds = home_page()
        self.ds.openurl(url)

    def test_login_01(self):
        pass
        # self.per.modify(u"wanhui","1",u"test",u"test","235323116",u"test信息")
        # self.per.msg()
        # self.assertEqual(u"wanhui",self.per.uName())


if __name__ == "__main__":
  unittest.main()



