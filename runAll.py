# _*_ coding:utf-8 _*_
import sys
import os
import unittest
from datetime import datetime
from framework import HTMLTestRunner
from framework import BSTestRunner
from loguru import logger
from framework import common

sys.path.append("../")

logger.info(f'正在检查testReports,logs和screenshot文件夹下，是否有超过创建时间超过{common.get_yaml_config_file("config.yaml")["DAYS"]}天的目录.....')
common.cleanup_directory('testReports')
common.cleanup_directory('logs')
common.cleanup_directory('screenshot')

# 设置报告文件保存路径
# report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testReports\\', )

# 获取系统当前时间
# now = datetime.now().strftime('%Y-%m-%d-%H_%M_%S')

# 测试报告名称
report_name = common.saved_report('testReports')

# 加载testCase文件中测试用例
suite = unittest.TestLoader().discover("testCase")
# suite = unittest.defaultTestLoader.discover(test_case_dir, pattern='testbaidusearch.py')


if __name__ == '__main__':
    with open(report_name, 'wb') as f:
        # runner1 = HTMLTestRunner.HTMLTestRunner(stream=f, title="聊天室自动化测试报告", description="用例测试情况")
        runner2 = BSTestRunner.BSTestRunner(stream=f, title="聊天室自动化测试报告", description="用例测试情况")
        # 开始执行测试套件
        # runner1.run(suite)
        runner2.run(suite)
    # 测试结束之后，执行邮件发送报告
    # common.send_mail()
