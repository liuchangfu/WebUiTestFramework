# _*_ coding:utf-8 _*_
import unittest
from framework.logger import Logger
from selenium import webdriver
from BasePage.BaiDuPage import BaiDuSerach


mylog = Logger(logger="百度页面搜索页面").get_log()


class TestBaiDuSerach(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_serach(self):
        try:
            driver = self.driver
            url = 'https://www.baidu.com'
            mylog.info('百度页面搜索页面，测试开始....')
            page = BaiDuSerach(driver, url)
            page.open()
            page.serach_text_input('selenium')
            page.serach_click()
            page.driver_wait('selenium')
            self.assertEqual(page.get_title(), 'selenium_百度搜索')
            mylog.info('百度页面搜索页面,测试完成,预期结果与实际结果相符，测试通过!!!')
        except AssertionError as e:
            mylog.error("断言出现失败：%s" % e)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
