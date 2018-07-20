# coding=utf-8

from web.common.comm import Comm
from selenium.webdriver.common.action_chains import ActionChains
import time

class xf_login(Comm):
    name_locator = ("id","userAccount")
    password_locator = ("id","userPassword")
    submit_locator = ("id","login_button")

    def test(self,txt,locator):
        self.openurl("http://faxuan.net/")
        element=self.driver.find_element_by_link_text(txt)
        ActionChains(self.driver).move_to_element(element).perform()
        self.click(locator)
        self.driver.switch_to_window(self.driver.window_handles[1])
        print(self.driver.title)

    def input_name(self,name):
        self.send(self.name_locator,name)

    def input_password(self,pas):
        self.send(self.password_locator,pas)

    def input_submit(self):
        self.click(self.submit_locator)

   def title(self):
        tle=self.driver.title
        print(tle)
        try:
            if tle in self.driver.title:
                print('标题一致打开的页面正确')
        except Exception as msg:
            print("标题错误！")
