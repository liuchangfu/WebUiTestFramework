# _*_ coding:utf-8 _*_
import unittest
from framework.log import GetLog
from selenium import webdriver
from BasePage.ChatRoomPage import ChatRoomPage
import time
from loguru import logger
from framework.save_screenshot import SaveScreen
from ddt import ddt, unpack, data
from framework.readConfigYaml import GetYamlConfig
import datetime

class TestChatRoom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = GetYamlConfig.get_yaml_config()
        cls.url = cls.config['URL'] + 'room/xyft?roomId=xyft'
        cls.driver = webdriver.Chrome()
        logger.add(GetLog('已登录-聊天室页面测试').save_path(), format="{time:YYYY-MM-DD----HH:mm:ss}--{level}--{message}",
                   retention='7 days',
                   rotation='10 MB',
                   encoding='utf-8')
        cls.page = ChatRoomPage(cls.driver, cls.url)
        logger.info('正在打开网站:{}', cls.url)
        cls.page.open()
        logger.info('正在执行添加cookies操作')
        cls.page.add_cookies()

    def test_chatroom01(self):
        """已登录，不输入聊天信息，点击发送按钮，校验弹出提示信息"""
        try:
            logger.info('T-已登录，不输入聊天信息，点击发送按钮，校验弹出提示信息。')
            self.page.click2()
            text = self.page.get_text2()
            time.sleep(3)
            self.assertEqual(text, '內容不能為空')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text, '內容不能為空')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8', level='ERROR')
            logger.error('T-已登录，不输入聊天信息，点击发送按钮，校验弹出提示信息，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text, '內容不能為空')
            directory = SaveScreen('test_chatroom01-错误截图').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出错啦，出错原因：{}', msg)

    def test_chatroom02(self):
        """已登录，输入发言信息后，正常发送"""
        try:
            logger.info('T-已登录，输入发言信息后，正常发送。')
            self.page.wait(3)
            text1 = '测试聊天信息' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            logger.info('正在输入聊天信息：{}', text1)
            self.page.input_chat_info(text1)
            time.sleep(3)
            logger.info('点击发送')
            self.page.click2()
            time.sleep(3)
            text2 = self.page.get_chat_texts()
            self.assertIn(text1, text2)
            logger.info('发送成功的聊天信息包含在聊天室显示区域中，测试通过。')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8', level='ERROR')
            logger.error('输入的发言信息不能正常发送！！')
            directory = SaveScreen('test_chatroom02-错误截图').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出错啦，出错原因：{}', msg)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
