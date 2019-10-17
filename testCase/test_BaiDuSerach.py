# _*_ coding:utf-8 _*_
import unittest
from framework.logger import Logger
from framework.log import GetLog
from selenium import webdriver
from BasePage.BaiDuPage import BaiDuSerach
from ddt import ddt, unpack, data
import time
from loguru import logger


# mylog = Logger(logger="百度页面搜索页面").get_log()


@ddt
class TestBaiDu_Serach(unittest.TestCase):
    """
    测试类方法，该类必继承unittest.TestCase类
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        logger.add(GetLog('百度搜索页面测试').save_path(), format="{time:YYYY-MM-DD at HH:mm:ss}--{level}--{message}",
                   retention='7 days',
                   rotation='10 MB')

    @data(['seleniun', 'selenium_百度搜索'], ['java', 'java_百度搜索'], ['php', 'php_百度搜索'])
    @unpack
    # 测试用例，输入搜索关键词，最后加入断言
    def test_serach(self, keyword, result):
        """百度搜索测试"""
        try:
            driver = self.driver
            url = 'https://www.baidu.com'
            logger.info('百度页面搜索页面，测试开始....')
            # mylog.info('百度页面搜索页面，测试开始....')
            page = BaiDuSerach(driver, url)
            logger.info('正在打开页面：{}', url)
            page.open()
            logger.info('输入查询关键词：{}', keyword)
            page.serach_text_input(keyword)
            page.serach_click()
            page.driver_wait(keyword)
            time.sleep(3)
            print(page.get_page_source())
            logger.info('断言校验开始')
            self.assertEqual(page.get_title(), result)
            logger.info('百度搜索页面，预期结果:{},实际结果:{}', keyword, result)
            # mylog.info('百度页面搜索,测试完成,预期结果与实际结果相符，测试通过!!!')
        except AssertionError:
            # mylog.error("断言失败，搜索关键词为：%s，实际结果为：%s" % (keyword, result))
            logger.info('百度搜索页面断言失败，预期结果:{},实际结果:{}', keyword, result)
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
