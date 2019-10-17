import sys

sys.path.append("../")
import os
import unittest
import time
from framework import HTMLTestRunner
from framework.SendEmail import SendMail
from framework.save_report import SaveReport
from loguru import logger

# 设置报告文件保存路径
report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testReports\\', )

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = SaveReport().save_path()
logger.info('打印报告目录:{}', HtmlFile)
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.TestLoader().discover("testCase")

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试报告", description="用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    fp.close()
    # 测试结束之后，执行邮件发送报告
    sendMail = SendMail()
    sendMail.send()
