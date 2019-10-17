# _*_ coding:utf-8 _*_
import os
import time
from loguru import logger


class Save_Screen(object):

    def __init__(self, name):
        self.name = name
        self.dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshot\\')
        self.directory_created_time = time.strftime('%Y-%m-%d', time.localtime())
        self.file_create_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime())

    def save_screen(self):
        try:
            global save_directory
            save_directory = self.dir + self.directory_created_time + '\\'
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
                logger.info('目录新建成功：{}', save_directory)
        except BaseException as msg:
            logger.info('新建目录失败：', msg)
        save_directory = self.dir + self.directory_created_time + '\\' + self.name + '_' + self.file_create_time + '.png'
        logger.info('截屏文件保存目录为:{}', save_directory)
        return save_directory



s1 = Save_Screen('test').save_screen()
