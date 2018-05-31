# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Comm():
    def __init__(self,browser=''):
        try:
            if browser == 'ff' or browser == 'Firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'ch' or browser == 'Chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'ie'  or browser == 'IE':
                self.driver = webdriver.Ie()
        except ValueError:
            print('Please enter the correct browser name!(Supported browsers are: Firefox、Chrome and Ie)')

   # url打开
    def openurl(self,url):
        self.driver.get(url)
        self.driver.maximize_window() #最大化浏览器

   # 定义元素获取
    def element(self,id,value):
        self.id=id
        self.value=value
        self.element = self.driver.find_element(id,value)
        return self.element


    # 点击功能
    def click(self):
          self.element.click()

   # 输入信息
    def send(self,txt):
        self.element.clear()
        self.element.send_keys(txt)


   # 显示等待
    def WebDriver(self,timeout,method):
        try:
          WebDriverWait(self.driver,timeout,5).until(method)
        except Exception as msg:
            print("Error:%s" % msg)

    # 隐示等待
    def implicitly(self,value):
        self.driver.implicitly_wait(value)

    # 截图

