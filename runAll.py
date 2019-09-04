import sys
sys.path.append("../")
import HTMLTestRunner
import os
import unittest
import time
from framework.SendEmail import SendMail

# 设置报告文件保存路径
report_path = os.path.abspath(os.curdir) + '/testReports/'
print(report_path)

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + ".html"
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.TestLoader().discover("testCase")
print(suite)

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="项目接口自动化测试报告", description="用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    fp.close()
    # 测试结束之后，执行邮件发送报告
    # sendMail = SendMail()
    # sendMail.send()
