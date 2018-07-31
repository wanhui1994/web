#coding=utf-8
import unittest
import HTMLTestRunner
from web.blog.fxshop.blog_login_xf_page import xf_login
from web.common.query import Py
import time




class ds_xf_login(unittest.TestCase):

    def setUp(self):
        self.drver = xf_login()
        self.py = Py()

    def test_login_01(self):
        for i in range(len(Py().code_href())):
            url="http://www.faxuan.net"+self.py.code_href()[i]
            self.drver.silent()
            self.drver.openurl(url)
            self.drver.page_timeout(5)
            self.drver.WebDriver(1,lambda driver : driver.find_element_by_id('userAccount'))
            self.drver.login("9876543210048","ceshi123","2f56fe3477f774c4ece2b926070b6d0a")
            self.drver.input_submit()
            time.sleep(2)
            self.drver.handel(-1)
            self.drver.title("法宣在线")
            self.drver.close()
            self.drver.handel(0)





if __name__ == "__main__":
  unittest.main()



