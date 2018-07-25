# coding=utf-8
from web.blog.fxshop.blog_login_ds_page import ds_login

from web.common.query import Py

class cc():

  def set_up(self):
      pass
  def test_login(self):
        for i in range(len(Py().code_href())):
          url="http://www.faxuan.net"
          print(url+Py().code_href()[i])

m=cc()
m.test_login()



