# _*_ coding:utf-8 _*_
from selenium import webdriver
import unittest
from loguru import logger
from framework import common
from Base.chatroompage import ChatRoomPage


class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.add(common.saved_log('login_test_chatroom_log'),
                   format="{time:YYYY-MM-DD----HH:mm:ss}--{level}--{message}",
                   rotation='10 MB',
                   encoding='utf-8')
        logger.info('==========setUp==========')
        cls.data = common.get_yaml_config_file('config.yaml')
        cls.url = cls.data['URL'] + 'room/xyft?roomId=xyft'
        logger.info(f'当前打开的网址为：{cls.url}"')
        cls.driver = webdriver.Chrome()
        cls.page = ChatRoomPage(cls.driver, cls.url)
        cls.page.open()
        logger.info('正在执行添加cookies操作')
        cls.page.imp_wait(5)
        cls.page.add_cookies()

    @classmethod
    def tearDownClass(cls):
        logger.info('==========tearDown=========')
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
