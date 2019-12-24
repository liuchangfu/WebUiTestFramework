# _*_ coding:utf-8 _*_
import unittest
from framework import common
from selenium import webdriver
from Base.chatroompage import ChatRoomPage
import time
from loguru import logger
from ddt import ddt, unpack, data
from framework.myunit import StartEnd


class TestCharRoom(StartEnd):

    @unittest.skip
    def test_chat_room01(self):
        try:
            logger.info('T-未登录,直接点击发送按钮，能否弹出提示信息')
            toast = self.page.click_send_btn_is_displayed()
            self.page.imp_wait(3)
            self.assertTrue(toast, True)
            logger.success(f'预期结果：{toast},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chatroom01', toast, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room01'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    @unittest.skip
    def test_chat_room02(self):
        try:
            logger.info('T-未登录,点击登录链接，是否弹出登录对话框')
            text1 = self.page.click_login_link()
            self.page.imp_wait(3)
            self.assertEqual(text1, '馬上登錄')
            logger.success(f'预期结果：{text1},实际结果为：{"馬上登錄"},测试通过！！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room02', text1, '馬上登錄')
            self.page.save_screens(common.saved_screenshot('test_chat_room02'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    @unittest.skip
    def test_chat_room03(self):
        try:
            logger.info('T-未登录，聊天输入框默认文本显示')
            text2 = self.page.get_chat_msg()
            self.page.imp_wait(3)
            self.assertEqual(text2, '登錄后才可以聊天哦！')
            logger.success(f'预期结果：{text2},实际结果为：{"登錄后才可以聊天哦！"},测试通过！！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room03', text2, '登錄后才可以聊天哦')
            self.page.save_screens(common.saved_screenshot('test_chatroom03'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    @unittest.skip
    def test_chat_room04(self):
        try:
            logger.info('T-未登录，点击只看关注按钮，能否弹出提示信息')
            toast = self.page.click_send_btn_is_displayed()
            self.page.imp_wait(3)
            self.assertTrue(toast, True)
            logger.success(f'预期结果：{toast},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room04', toast, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room04'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    @unittest.skip
    def test_chat_room05(self):
        try:
            logger.info('T-点击夜间模式，样式能否切换')
            value = self.page.click_night_btn()
            self.page.imp_wait(3)
            self.assertEqual(value, 'chat night-skin')
            logger.success(f'预期结果：{value},实际结果：{"chat night-skin"}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room05', value, "chat night-skin")
            self.page.save_screens(common.saved_screenshot('test_chat_room05'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    @unittest.skip
    def test_chat_room06(self):
        try:
            logger.info('T-未登录，点击聊天信息区用户头像，能否弹出提示信息')
            toast = self.page.click_avatar()
            self.page.imp_wait(3)
            self.assertTrue(toast, True)
            logger.success(f'预期结果：{toast},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room06', toast, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room06'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    @unittest.skip
    def test_chat_room07(self):
        try:
            logger.info('T-未登录，点击主播推荐中的关注按钮，能否弹出登录对话框')
            text = self.page.anchor_follow_btn()
            self.page.imp_wait(3)
            self.assertEqual(text, '馬上登錄')
            logger.success(f'预期结果：{text},实际结果：{"馬上登錄"}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room07', text, "馬上登錄")
            self.page.save_screens(common.saved_screenshot('test_chat_room07'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    def test_chat_room08(self):
        try:
            logger.info('T-未登录，在线用户列中的关注按钮，能否弹出登录对话框')
            text = self.page.click_online_user_btn()
            self.page.imp_wait(3)
            self.assertEqual(text, '馬上登錄')
            logger.success(f'预期结果：{text},实际结果：{"馬上登錄"}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room08', text, "馬上登錄")
            self.page.save_screens(common.saved_screenshot('test_chat_room08'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    def test_chat_room09(self):
        try:
            logger.info('T-未登录，我的关注，能否弹出登录对话框')
            text = self.page.click_my_focus_link()
            self.page.imp_wait(3)
            self.assertEqual(text, '馬上登錄')
            logger.success(f'预期结果：{text},实际结果：{"馬上登錄"}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room09', text, "馬上登錄")
            self.page.save_screens(common.saved_screenshot('test_chat_room09'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')


if __name__ == '__main__':
    unittest.main()
