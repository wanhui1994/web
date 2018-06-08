# coding=utf-8
from web.common.comm import Comm
import time
from selenium import webdriver

class ds_login(Comm):
    name_locator = ("id","userAccount")
    password_locator = ("id","userPassword")
    submit_locator = ("id","submitLogin")

    def input_name(self,name):

        self.send(self.name_locator,name)

    def input_password(self,pas):
        self.send(self.password_locator,pas)

    # def input_checkcode(self,code):
    #      self.send()

    def input_submit(self):
        self.click(self.submit_locator)


    def login(self,name,pas):
        self.input_name(name)
        self.input_password(pas)



    # 其他方式登录
if __name__ == "__main__":
    c=ds_login()
    c.openurl("http://faxuan.net/bps/login/t/login_1_t.html?return_url=/")
    c.login("15011530850","ceshi123")
    time.sleep(5)
    c.input_submit()