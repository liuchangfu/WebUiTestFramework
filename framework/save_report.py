# _*_ coding:utf-8 _*_
import os
import time
from loguru import logger


class SaveReport(object):

    def __init__(self):
        self.dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testReports\\')
        self.report_create_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime())
        self.directory_created_time = time.strftime('%Y-%m-%d', time.localtime())

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
