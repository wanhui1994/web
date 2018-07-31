# coding=utf-8
from web.common.comm import Comm
url = "http://faxuan.net"
class home_page(Comm):

    def login(self):
        login_locator=("xpath",".//*[@id='hfright']/a[1]")
        self.click(login_locator)

    def userhome(self):
        '''点击用户中心图标'''
        login_locator=("id","gouserhome")
        self.click(login_locator)

