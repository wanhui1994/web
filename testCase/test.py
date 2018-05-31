# coding=utf-8

from web.common.comm import Comm
from selenium.webdriver.support import expected_conditions as EC
a = 'ff'
# Comm.openurl("https://www.baidu.com/")
driver = Comm(a)
driver.openurl("https://www.baidu.com/")
b=EC.title_is("111")
driver.WebDriver(0,b)
# a=5
# b=0
# try:
#   c=a/b
# except Exception as msg:
#     print(msg)

