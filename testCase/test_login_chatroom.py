# _*_ coding:utf-8 _*_
import unittest
from framework import common
import time
from loguru import logger
from ddt import ddt, unpack, data
from framework.login_myunit import StartEnd


class TestCharRoom(StartEnd):

    @unittest.skip
    def test_chat_room01(self):
        try:
            logger.info('T-已登录,发送聊天信息')
            text = '测试信息'
            result = self.page.enter_msg_send(text)
            self.page.imp_wait(3)
            self.assertTrue(result, True)
            logger.success(f'预期结果：{result},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-login_test_chat_room', 'test_chat_room01', result, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room01'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    @unittest.skip
    def test_chat_room02(self):
        try:
            logger.info('T-已登录,直接点击发送按钮')
            result = self.page.click_send_btn_is_displayed()
            self.page.imp_wait(3)
            self.assertTrue(result, True)
            logger.success(f'预期结果：{result},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-login_test_chat_room', 'test_chat_room02', result, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room02'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    @unittest.skip('发送表情暂时无法验证')
    def test_chat_room03(self):
        try:
            logger.info('T-已登录,发送表情')
            result = self.page.send_emoji()
            self.page.imp_wait(3)
            self.assertTrue(result, True)
            logger.success(f'预期结果：{result},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-login_test_chat_room', 'test_chat_room03', result, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room03'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    def test_chat_room04(self):
        try:
            logger.info('T-已登录,关注主播')
            result = self.page.chat_anchor_list()
            self.page.imp_wait(3)
            self.assertTrue(result, True)
            logger.success(f'预期结果：{result},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-login_test_chat_room', 'test_chat_room04', result, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room04'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)


if __name__ == '__main__':
    unittest.main()