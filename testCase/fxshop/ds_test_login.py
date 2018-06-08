# coding=utf-8
from selenium import webdriver
from web.blog.fxshop.blog_login_ds_page import ds_login
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import HTMLTestRunner

class Login_test_ds(unittest.TestCase):
    def setUp(self):
         self.login=ds_login()
         self.login.openurl("http://faxuan.net/bps/login/t/login_1_t.html?return_url=/")

    def test_login_01(self):
        self.login.input_name("15011530850")
        self.login.input_password("ceshi123")
        time.sleep(5)
        self.login.input_submit()



if __name__ == "__main__":
    now=time.strptime("%Y-%m-%d %H_%M_%S")
    filename="E:\\py-wh-lx\\web\\report\\"+now+"resut.html"
    fp=open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=filename,title=u"自动化测试",description=u'用例执行情况：')
    runner.run(Login_test_ds())
    fp.close()
