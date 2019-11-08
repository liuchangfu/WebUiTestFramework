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
import requests


class TestChatRoom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = GetYamlConfig.get_yaml_config()
        cls.url = cls.config['URL'] + 'room/xyft?roomId=xyft'
        cls.driver = webdriver.Chrome()
        cls.header = {
                    "Accept": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
                    "Content-Type": "application/json",
                    "Cookie": "KX_LIVE_UUID={};KX_LIVE_TK={}".format(cls.config['COOKES'][1]['VAULE2'],
                                                                     cls.config['COOKES'][0]['VAULE1'])
                    }
        logger.add(GetLog('已登录---聊天室页面测试').save_path(), format="{time:YYYY-MM-DD----HH:mm:ss}--{level}--{message}",
                   retention='7 days',
                   rotation='10 MB',
                   encoding='utf-8')
        cls.page = ChatRoomPage(cls.driver, cls.url)
        logger.info('正在打开网站:{}', cls.url)
        cls.page.open()
        logger.info('正在执行添加cookies操作')
        cls.page.add_cookies()
        cls.page.wait(5)

    def test_chatroom01(self):
        """已登录，点击发送按钮，校验弹出提示信息"""
        try:
            logger.info('T-已登录，点击发送按钮，校验弹出提示信息。')
            self.page.click2()
            self.page.wait(2)
            text = self.page.get_text2()
            self.assertEqual(text, '內容不能為空')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text, '內容不能為空')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8', level='ERROR')
            logger.error('T-已登录，点击发送按钮，校验弹出提示信息，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text, '內容不能為空')
            directory = SaveScreen('错误截图').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题咬掉，请检查！！报错的信息为：{}', msg)

    def test_chatroom2(self):
        """已登录，输入发言信息后，正常发送"""
        try:
            logger.info('T-已登录，输入发言信息后，正常发送。')
            self.page.wait(3)
            text = '测试聊天信息'
            logger.info('正在输入聊天信息：{}', text)
            self.page.input_chat_info(text)
            logger.info('点击发送')
            self.page.click2()
            time.sleep(5)
            # 构造接口数据
            data = {"roomCode": "xyft", "content": text, "toId": "", "isTop": 0}
            response = requests.post("http://kx.1396c.com/api/chat/say?r=0.45836299015915594", headers=self.header,
                                     json=data)
            # 获取发言成功的状态
            result = response.status_code
            self.assertEqual(result, 200)
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8', level='ERROR')
            logger.error('T-已登录，输入发言信息后，能正常发送。预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', result, '接口返回状态非200！！')
            directory = SaveScreen('错误截图').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，请检查代码！！报错的信息为：{}', msg)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
