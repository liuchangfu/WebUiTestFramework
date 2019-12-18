# _*_ coding:utf-8 _*_
from selenium import webdriver
import unittest
from loguru import logger
from framework import common


class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info('==========setUp==========')
        cls.driver = webdriver.Chrome()
        cls.url = 'https://www.baidu.com'
        logger.add(common.saved_log('logs', '百度搜索页面测试'),
                   format="{time:YYYY-MM-DD at HH:mm:ss}--{level}--{message}",
                   retention='7 days',
                   rotation='10 MB',
                   encoding='utf-8')

    @classmethod
    def tearDownClass(cls):
        logger.info('==========tearDown=========')
        cls.driver.quit()
