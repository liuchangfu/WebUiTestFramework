# _*_ coding: utf-8 _*_
import logging
import os.path
import time


class Logger(object):
    '''
    指定保存日志的文件路径，日志级别，以及将日志存入到指定的文件中
    '''

    def __init__(self, logger):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 获取当前时间
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 获取当前日志的目录
        log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        # log_path = os.path.abspath(os.curdir) + '/logs/'
        # 日志文件的名字
        log_name = log_path + rq + '.txt'

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_name, encoding='utf-8')
        # 设置消息级别
        fh.setLevel(logging.INFO)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        # 设置消息级别
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
