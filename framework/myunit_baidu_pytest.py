# _*_ coding:utf-8 _*_
from selenium import webdriver
from loguru import logger
from framework import common
from Base.baidupage import BaiDuSearch


class StartEnd(object):

    def setup_class(self):
        logger.info('==========setUp==========')
        self.driver = webdriver.Chrome()
        self.url = 'https://www.baidu.com'
        logger.add(common.saved_log('百度搜索页面测试'),
                   format="{time:YYYY-MM-DD at HH:mm:ss}--{level}--{message}",
                   retention='7 days',
                   rotation='10 MB',
                   encoding='utf-8')

    def teardown_class(self):
        logger.info('==========tearDown=========')
        self.driver.quit()
