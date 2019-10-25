# _*_ coding:utf-8 _*_
import unittest
from framework.log import GetLog
from selenium import webdriver
from BasePage.ChatRoomPage import ChatRoomPage
import time
from loguru import logger
from framework.save_screenshot import SaveScreen


class TestCharRoom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        logger.add(GetLog('聊天室页面测试').save_path(), format="{time:YYYY-MM-DD at HH:mm:ss}--{level}--{message}",
                   retention='7 days',
                   rotation='10 MB',
                   encoding='utf-8')

    def test_chatroom_01(self):

        driver = self.driver
        url = 'http://kx.1396c.com/'
        logger.info('聊天室页面功能测试开始！')
        page = ChatRoomPage(driver, url)
        logger.info('正在打开主页：{}', url)
        page.open()
        page.wait(3)
        page.switch_click()
        logger.info('正在切换窗口！！')
        page.wait(3)
        page.switch_to_window()
        text = page.input_text()
        logger.info(text)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
