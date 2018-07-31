#coding=utf-8

from web.common.comm import Comm
import time

class Login_xf():
    name_locator = ("id","userAccount")
    password_locator = ("id","userPassword")
    submit_locator = ("xpath","html/body/div[4]/div[1]/a[1]")
    code_locator=("id","usercheckcode")

    def __init__(self):
        self.comm = Comm()

    def input_name(self,name):
        self.comm.send(self.name_locator,name)

    def input_password(self,pas):
         self.comm.send(self.password_locator,pas)

    def input_checkcode(self,code):
          self.comm.send(self.code_locator,code)

    def input_submit(self):
         self.comm.click(self.submit_locator)

    def close(self):
         self.comm.driver.close()

    def handel(self,num):
        allhandel =  self.comm.driver.window_handles
        return self.comm.driver.switch_to.window(allhandel[num])

    def title(self,name):
        title = self.comm.driver.title
        if title == name:
            print("校验页面打开正确")
        else:
            print("页面校验失败",title)

    # 切换到子站的页面
    def qh(self):
        for i in range(31):
           path1="html/body/div[6]/div[1]/div[1]/ul/li["
           path2="]/a"
           self.comm.driver.find_element_by_xpath(path1).click()

    def login(self, name, pas, code):
        self.input_name(name)
        self.input_password(pas)
        self.input_checkcode(code)


class Login_ds():
     name_locator = ("xpath",".//*[@id='userAccount']")
     password_locator = ("xpath",".//*[@id='userPassword']")
     submit_locator = ("xpath",".//*[@id='submitLogin']")
     code_locator=("id","usercheckcode")

     def __init__(self):
         self.comm = Comm()

     def input_name(self,name):
         self.comm.send(self.name_locator,name)

     def input_password(self,pas):
         self.comm.send(self.password_locator,pas)

     # 由于设置新的验证码耗费时间较长，暂时用手动代替
     def input_checkcode(self,code):
         self.comm.send(self.code_locator,code)

     def click_submit(self):
         self.comm.click(self.submit_locator)

     def login(self,name,pas):
         self.input_name(name)
         self.input_password(pas)
         time.sleep(5)
         self.click_submit()
