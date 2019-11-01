# _*_ coding:utf-8 _*_
import unittest
from framework.log import GetLog
from selenium import webdriver
from BasePage.ChatRoomPage import ChatRoomPage
import time
from loguru import logger
from framework.save_screenshot import SaveScreen
from ddt import ddt, unpack, data


class TestCharRoom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://kx.1396c.com/room/xyft?roomId=xyft'
        cls.driver = webdriver.Chrome()
        logger.add(GetLog('未登录---聊天室页面测试').save_path(), format="{time:YYYY-MM-DD----HH:mm:ss}--{level}--{message}",
                   retention='7 days',
                   rotation='10 MB',
                   encoding='utf-8')
        cls.page = ChatRoomPage(cls.driver, cls.url)
        logger.info('正在打开网站:{}', cls.url)
        cls.page.open()

    def test_chatroom1(self):
        """未登录:校验聊天输入框默认显示文本"""
        try:
            # page.switch_click()
            # page.wait(3)
            # page.switch_handler()
            logger.info('T-未登录:校验聊天输入框默认显示文本')
            text1 = self.page.input_text1()
            self.assertEqual(text1, '登錄后才可以聊天哦！')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text1, '登錄后才可以聊天哦！')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            logger.error('未登录:校验聊天输入框默认显示文本，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text1, '登錄后才可以聊天哦！')
            directory = SaveScreen('聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise

    def test_chatroom2(self):
        """未登录：点击发送按钮，校验弹出提示信息"""
        try:
            logger.info('T-未登录：点击发送按钮，校验弹出提示信息')
            self.page.click2()
            text2 = self.page.input_text2()
            self.assertEqual(text2, '親，需要登錄才有發言權限哦！')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text2, '親，需要登錄才有發言權限哦！')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            logger.error('未登录：点击发送按钮，校验弹出提示信息，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text2, '親，需要登錄才有發言權限哦！')
            directory = SaveScreen('聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise

    def test_chatroom3(self):
        """未登录:点击聊天信息输入框的登录链接，能否弹出登录对话框"""
        try:
            logger.info('T-未登录:点击聊天信息输入框的登录链接，能否弹出登录对话框')
            self.page.click3()
            text3 = self.page.input_text3()
            self.assertEqual(text3, '馬上登錄')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text3, '馬上登錄')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            logger.error('未登录:点击聊天信息输入框的登录链接，能否弹出登录对话框，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text3, '馬上登錄')
            directory = SaveScreen('聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
