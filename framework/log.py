# _*_ coding:utf-8 _*_
from loguru import logger
import os
import time


class GetLog(object):

    def __init__(self, name):
        self.name = name
        self.directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs\\')
        try:
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
                logger.info('目录新建成功:{}', self.directory)
        except BaseException as msg:
            logger.info('新建目录失败：', msg)
        self.directory_created_time = time.strftime('%Y-%m-%d', time.localtime())

    def save_path(self):
        global save_directory
        try:
            save_directory = self.directory + self.directory_created_time + '\\'
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
                logger.info('目录新建成功：{}', save_directory)
        except BaseException as msg:
            logger.info('新建目录失败：', msg)
        path = save_directory + self.name + '.txt'
        logger.info('日志保存目录为:{}', path)
        return path

# l1  = GetLog('aa').save_path()
