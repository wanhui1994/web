# coding=utf-8

from pyweb.web.common.comm import Comm1
from selenium.webdriver.support import expected_conditions as EC
a = 'ff'
# Comm.openurl("https://www.baidu.com/")
driver = Comm1(a)
driver.openurl("https://www.baidu.com/")
b=EC.title_is(u"百度一下，你就知道1111")
driver.WebDriver(10,b)

