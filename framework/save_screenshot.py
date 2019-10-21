# _*_ coding:utf-8 _*_
import os
import time
from loguru import logger


class SaveScreen(object):
    """
    测试用例运行失败的截图，保存到指定目录，如当天的生成的目录不存在，则自动创建
    """

    # 初始化数据
    def __init__(self, name):
        self.name = name
        self.dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshot\\')
        try:
            if not os.path.exists(self.dir):
                os.makedirs(self.dir)
                logger.info('目录新建成功:{}', self.dir)
        except BaseException as msg:
            logger.info('新建目录失败：', msg)
        self.directory_created_time = time.strftime('%Y-%m-%d', time.localtime())
        self.file_create_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime())

    # 保存测试不通过用例截图到指定目录
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


# s1 = SaveScreen('test').save_screen()
