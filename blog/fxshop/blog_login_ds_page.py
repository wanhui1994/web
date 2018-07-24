# coding=utf-8

#学法电商子站登录
from web.common.comm import Comm
import time


class ds_login(Comm):
    name_locator = ("id","userAccount")
    password_locator = ("id","userPassword")
    submit_locator = ("className","login_button")
    code_locator=("id","usercheckcode")

    def input_name(self,name):
        self.send(self.name_locator,name)

    def input_password(self,pas):
        self.send(self.password_locator,pas)

    def input_checkcode(self,code):
         self.send(self.code_locator,code)

    def input_submit(self):
        self.click(self.submit_locator)

    def login(self, name, pas, code):
        self.input_name(name)
        self.input_password(pas)
        self.input_checkcode(code)

    def close(self):
        self.driver.close()

    def handel(self,num):
        allhandel = self.driver.window_handles
        return self.driver.switch_to.window(allhandel[num])

    def title(self,name):
        title = self.driver.title
        if title == name:
            print("校验页面打开正确")
        else:
            print("页面校验失败",title)

    # 切换到子站的页面
    def qh(self):
        path1="html/body/div[6]/div[1]/div[1]/ul/li["
        path2="]/a"
        self.driver.find_element_by_xpath(path1).click()

