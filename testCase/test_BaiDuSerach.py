# _*_ coding:utf-8 _*_
import unittest
from framework.logger import Logger
from selenium import webdriver
from BasePage.BaiDuPage import BaiDuSerach
from ddt import ddt, unpack, data
import time

mylog = Logger(logger="百度页面搜索页面").get_log()


@ddt
class TestBaiDuSerach(unittest.TestCase):
    """
    测试类方法，该类必继承unittest.TestCase类
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @data(['seleniun', 'selenium_百度搜索'], ['java', 'java_百度搜索'], ['php', 'php_百度搜索'])
    @unpack
    # 测试用例，输入搜索关键词，最后加入断言
    def test_serach(self, keyword, result):
        """百度搜索测试"""
        try:
            driver = self.driver
            url = 'https://www.baidu.com'
            mylog.info('百度页面搜索页面，测试开始....')
            page = BaiDuSerach(driver, url)
            page.open()
            page.serach_text_input(keyword)
            page.serach_click()
            page.driver_wait(keyword)
            time.sleep(3)
            print(page.get_page_source())
            self.assertEqual(page.get_title(), result)
            mylog.info('百度页面搜索,测试完成,预期结果与实际结果相符，测试通过!!!')
        except AssertionError:
            mylog.error("断言失败，搜索关键词为：%s，实际结果为：%s" % (keyword, result))
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
