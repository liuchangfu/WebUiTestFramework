# _*_ coding:utf-8 _*_
import os
import time
from loguru import logger


class SaveReport(object):
    """
    测试报告保存到指定目录，如当天的生成的测试报告目录不存在，则自动创建
    """

    # 初始化数据
    def __init__(self):
        self.dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testReports\\')
        try:
            if not os.path.exists(self.dir):
                os.makedirs(self.dir)
                logger.info('目录新建成功:{}', self.dir)
        except BaseException as msg:
            logger.info('新建目录失败：', msg)
        self.report_create_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime())
        self.directory_created_time = time.strftime('%Y-%m-%d', time.localtime())

    # 保存测试报告到指定的目录
    def save_path(self):
        try:
            global save_directory
            save_directory = self.dir + self.directory_created_time + '\\'
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
                logger.info('目录新建成功：{}', save_directory)
        except BaseException as msg:
            logger.info('新建目录失败：', msg)
        path = save_directory + self.report_create_time + '.html'
        logger.info('测试报告保存目录为:{}', path)
        return path

# s1 = SaveReport().save_path()
