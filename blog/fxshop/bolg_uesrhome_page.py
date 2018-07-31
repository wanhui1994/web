# coding=utf-8
'''个人中心的页面元素'''

from web.common.comm import Comm

class personal(Comm):

    def information(self):
        user_locator = ("xpath","html/body/div[7]/div[1]/div/ul/li[1]/div[2]/ul/li[1]/a")
        self.click(user_locator)  #点击基本信息
        user_modify=("xpath",".//*[@id='content']/div/h3/a") #点击修改
        self.click(user_modify)

    def username(self,name):
        name_locator = ("id","realname")  #用户姓名
        self.send(name_locator,name)

    def radio(self):
        radio_locator = ("xpath",".//*[@id='content']/div[1]/div[4]/div[2]/label[2]") #性别:女
        self.click(radio_locator)

    def region(self):
        #地区选择
        region01_locator=("xpath",".//*[@id='content']/div[1]/div[5]/div[2]/div[1]/a") #第一个下拉列表
        region02_locator = ("xpath",".//*[@id='content']/div[1]/div[5]/div[2]/div[2]/a")
        region03_locator = ("xpath",".//*[@id='content']/div[1]/div[5]/div[2]/div[3]/a")
        data01_locactor = ("xpath",".//*[@id='province']/li[15]")#省级
        data02_locactor = ("xpath",".//*[@id='city']/li[6]") #市级
        data03_locactor = ("xpath",".//*[@id='county']/li[5]") #县级
        self.click(region01_locator)
        self.click(data01_locactor)
        self.click(region02_locator)
        self.click(data02_locactor)
        self.click(region03_locator)
        self.click(data03_locactor)

    def address(self,addre):
        #添加地区信息
        address_locactor = ("id","address")
        self.send(address_locactor,addre)

    def company(self,comp):
        #添加单位信息
        company_locactor = ("id","company")
        self.send(company_locactor,comp)

    def position(self,post):
         title_locactor = ("id","title")
         self.send(title_locactor,post)

    def qiu(self,qq):
        #QQ号添加
        qq_locactor = ("id","qq")
        self.send(qq_locactor,qq)

    def synopsis(self,pro):
        #个人简介
        proflie_locactor = ("id","proflie")
        self.send(proflie_locactor,pro)

    def permit(self):
        #允许公开
        gongkai_locactor = ("id","gongkai")
        self.click(gongkai_locactor)

    def submit(self):
        submit_locator = ("xpath",".//*[@id='content']/div[1]/div[14]/div[2]/a")
        self.click(submit_locator)

    def msg(self):
        #修改点击确定按钮
        msg_locator=("xpath",".//*[@id='content']/div[3]/div[2]/a")
        self.click(msg_locator)

    def modify(self,name,addre,comp,post,qq,pro):
        '''修改方法'''
        self.uname=name
        self.username(name)
        self.radio()
        self.region()
        self.address(addre)
        self.company(comp)
        self.position(post)
        self.qiu(qq)
        self.synopsis(pro)
        self.permit()
        self.submit()

    #获取添加的元素信息
    def uName(self):
        locator=("id","uName")
        self.text(locator) #获得修改后的姓名信息

    def uSex(self):
        self.usex = self.driver.find_element("id","uSex").text    #获得修改后的性别字段
        return self.usex
    def uCity(self):
        self.ucity = self.driver.find_element("id","uCity").text  #获得修改后的地区字段
        return self.ucity
    def uAddr(self):
        self.uaddr = self.driver.find_element("id","uAddr").text  #获得修改后的地址字段
        return self.uaddr
    def uDomain(self):
        self.udomain = self.driver.find_element("id","uDomain").text #获得修改后的单位字段
        return self.udomain
    def uPost(self):
        self.upost = self.driver.find_element("id","uPost").text  #获得修改后的职务字段
        return self.upost
    def uqq(self):
        self.uqq = self.driver.find_element("id","uQQ").text      #获得修改后的扣扣字段
        return self.uqq
    def uProfile(self):
        self.uprofile = self.driver.find_element("id","uProfile").text     #获得修改后的简介字段
        return  self.uprofile

