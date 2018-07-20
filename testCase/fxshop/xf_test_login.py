# codign=utf-8
# from web.common.comm import Comm
from selenium import webdriver
import time

url="http://faxuan.net/"
driver=webdriver.Firefox()
driver.get(url)
time.sleep(10)
