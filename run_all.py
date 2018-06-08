# coding=utf-8
import HTMLTestRunner
import unittest
import time
import sys,os

# cur_path= "E:\\py-wh-lx\\web\\testCase\\fxshop\\ds_test_login.py"

def add_case():
    case_path="E:\\py-wh-lx\\web\\testCase\\fxshop\\ds_test_login.py"
    discover = unittest.defaultTestLoader.discover(case_path)
    print(discover)
    return discover

def run_case(all_case):
    now=time.strptime("%Y-%m-%d %H_%M_%S")
    filename="E:\\py-wh-lx\\web\\report\\"+now+"resut.html"
    fp=open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=filename,title=u"自动化测试",description=u'用例执行情况：')
    runner.run(all_case)
    fp.close()
def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(case_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


if __name__ == "__main__":
    all_case=add_case()
    run_case(all_case)
    report_path="E:\\py-wh-lx\\web\\testCase\\fxshop"
    report_file=get_re
