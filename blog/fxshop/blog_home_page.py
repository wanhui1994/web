# coding=utf-8
from web.common.comm import Comm

class home_page():
    def __init__(self):
        self.c = Comm()
    def login(self):
        self.c.element("xpath",".//*[@id='hfright']/a[1]")

    def register(self):
        self.c.element("xpath",".//*[@id='hfright']/a[2]")
