#coding=utf-8
import unittest
import HTMLTestRunner
from web.blog.fxshop.blog_login_ds_page import ds_login
from web.common.query import Py
from selenium.webdriver.support import expected_conditions as EC
import time


class ds_xf_login(unittest.TestCase):
    a=ds_login()
    a.openurl("http://www.faxuan.net")
    def set_up(self):
        # self.login = ds_login()
        # self.py01 = Py()
        # self.login.driver.get(url="http://www.faxuan.net/")
         pass

    def test_login_01(self):
        for i in range(len(Py().code_href())):
            url="http://www.faxuan.net"+Py().code_href()[i]
            self.a.openurl(url)
            self.a.page_timeout(5)
            self.a.WebDriver(1,lambda driver : driver.find_element_by_id('userAccount'))
            self.a.login("9876543210048","ceshi123","2f56fe3477f774c4ece2b926070b6d0a")
            self.a.input_submit()
            time.sleep(2)
            self.a.handel(-1)
            self.a.title("法宣在线")
            self.a.driver.quit()
            try:
                self.a.driver.refresh()
            except ConnectionRefusedError as e:
                print(e)
            finally:
                self.a.driver.command_executor.execute(command=)




if __name__ == "__main__":
  unittest.main()



