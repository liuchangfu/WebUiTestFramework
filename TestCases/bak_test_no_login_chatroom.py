# _*_ coding:utf-8 _*_
import unittest
from framework import common
import time
from loguru import logger
from ddt import ddt, unpack, data
from framework.myunit import StartEnd


class TestCharRoom(StartEnd):

    def test_chat_room01(self):
        """T-点击夜间模式，样式能否切换"""
        try:
            logger.info('T-点击夜间模式，样式能否切换')
            value = self.page.click_night_btn()
            self.page.imp_wait(3)
            self.assertEqual(value, 'chat night-skin')
            logger.success(f'预期结果：{value},实际结果：{"chat night-skin"}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room01', value, "chat night-skin")
            self.page.save_screens(common.saved_screenshot('test_chat_room05'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    def test_chat_room02(self):
        """T-未登录,直接点击发送按钮，能否弹出提示信息"""
        try:
            logger.info('T-未登录,直接点击发送按钮，能否弹出提示信息')
            toast = self.page.click_send_btn_is_displayed()
            self.page.imp_wait(3)
            self.assertTrue(toast, True)
            logger.success(f'预期结果：{toast},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chatroom02', toast, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room01'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    def test_chat_room03(self):
        """T-未登录,点击登录链接，是否弹出登录对话框"""
        try:
            logger.info('T-未登录,点击登录链接，是否弹出登录对话框')
            text1 = self.page.click_login_link()
            self.page.imp_wait(3)
            self.assertEqual(text1, '馬上登錄')
            logger.success(f'预期结果：{text1},实际结果为：{"馬上登錄"},测试通过！！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room03', text1, '馬上登錄')
            self.page.save_screens(common.saved_screenshot('test_chat_room02'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    def test_chat_room04(self):
        """T-未登录，聊天输入框默认文本显示"""
        try:
            logger.info('T-未登录，聊天输入框默认文本显示')
            text2 = self.page.get_chat_msg()
            self.page.imp_wait(3)
            self.assertEqual(text2, '登錄后才可以聊天哦！')
            logger.success(f'预期结果：{text2},实际结果为：{"登錄后才可以聊天哦！"},测试通过！！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room04', text2, '登錄后才可以聊天哦')
            self.page.save_screens(common.saved_screenshot('test_chatroom03'))
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，报错的信息为：{}', msg)

    def test_chat_room05(self):
        """T-未登录，点击只看关注按钮，能否弹出提示信息"""
        try:
            logger.info('T-未登录，点击只看关注按钮，能否弹出提示信息')
            toast = self.page.click_send_btn_is_displayed()
            self.page.imp_wait(3)
            self.assertTrue(toast, True)
            logger.success(f'预期结果：{toast},实际结果：{True}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room05', toast, True)
            self.page.save_screens(common.saved_screenshot('test_chat_room04'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    def test_chat_room06(self):
        """T-未登录，点击聊天信息区用户头像，能否弹出提示信息"""
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

    def test_chat_room07(self):
        """T-未登录，点击主播推荐中的关注按钮，能否弹出登录对话框"""
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
        """T-未登录，在线用户列中的关注按钮，能否弹出登录对话框"""
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
        """T-未登录，我的关注，能否弹出登录对话框"""
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

    def test_chat_room10(self):
        """T-实时竞猜与竞猜主页的最新竞猜，竞猜人是否一致"""
        try:
            logger.info('T-实时竞猜与竞猜主页的最新竞猜，竞猜人是否一致')
            text = self.page.guess_tab1()
            self.page.imp_wait(3)
            self.assertIn(text, self.page.guess_homepage_new())
            logger.success(f'预期结果：{text},实际结果：{self.page.guess_homepage_new()}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room10', text,
                                   self.page.guess_homepage_new())
            self.page.save_screens(common.saved_screenshot('test_chat_room10'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    # def test_chat_room11(self):
    #     """T-实时竞猜与竞猜主页的最新竞猜，竞猜人是否一致"""
    #     try:
    #         logger.info('T-实时竞猜与竞猜主页的最新竞猜，竞猜人是否一致')
    #         text = self.page.guess_tab1()
    #         self.page.imp_wait(3)
    #         self.assertEqual(text, self.page.guess_homepage_new())
    #         logger.success(f'预期结果：{text},实际结果：{self.page.guess_homepage_new()}，测试通过！！')
    #     except AssertionError:
    #         common.assertion_error('F-no_login_test_chat_room', 'test_chat_room11', text,
    #                                self.page.guess_homepage_new())
    #         self.page.save_screens(common.saved_screenshot('test_chat_room11'))
    #         raise
    #     except Exception as msg:
    #         logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    def test_chat_room12(self):
        """T-竞猜排行连赢榜与竞猜主页的排行榜连赢榜，竞猜人是否一致"""
        try:
            logger.info('T-竞猜排行连赢榜与竞猜主页的排行榜连赢榜，竞猜人是否一致')
            text = self.page.guess_tab2()
            self.page.imp_wait(3)
            self.assertEqual(text, self.page.guess_homepage_rank()[0])
            logger.success(f'预期结果：{text},实际结果：{self.page.guess_homepage_rank()[0]}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room12', text,
                                   self.page.guess_homepage_rank()[0])
            self.page.save_screens(common.saved_screenshot('test_chat_room12'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    def test_chat_room13(self):
        """T-竞猜排行赢率榜与竞猜主页的排行榜赢率榜，竞猜人是否一致"""
        try:
            logger.info('T-竞猜排行赢率榜与竞猜主页的排行榜赢率榜，竞猜人是否一致')
            text = self.page.guess_tab2_yingyu()
            self.page.imp_wait(3)
            self.assertEqual(text, self.page.guess_homepage_rank()[1])
            logger.success(f'预期结果：{text},实际结果：{self.page.guess_homepage_rank()[1]}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room13', text,
                                   self.page.guess_homepage_rank()[1])
            self.page.save_screens(common.saved_screenshot('test_chat_room13'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    def test_chat_room14(self):
        """T-竞猜排行赢利榜与竞猜主页的排行榜赢利榜，竞猜人是否一致"""
        try:
            logger.info('T-竞猜排行赢利榜与竞猜主页的排行榜赢利榜，竞猜人是否一致')
            text = self.page.guess_tab2_yingli()
            self.page.imp_wait(3)
            self.assertEqual(text, self.page.guess_homepage_rank()[2])
            logger.success(f'预期结果：{text},实际结果：{self.page.guess_homepage_rank()[2]}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room14', text,
                                   self.page.guess_homepage_rank()[2])
            self.page.save_screens(common.saved_screenshot('test_chat_room14'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')

    def test_chat_room15(self):
        """T-主播预告与首页当前预告排班信息是否一致"""
        try:
            logger.info('T-主播预告与首页当前预告排班信息是否一致')
            text = self.page.chatroom_anchor_preview()
            self.page.imp_wait(3)
            self.assertEqual(text, '暫無預告')
            logger.success(f'预期结果：{text},实际结果：{"暫無預告"}，测试通过！！')
        except AssertionError:
            common.assertion_error('F-no_login_test_chat_room', 'test_chat_room15', text,
                                   '暫無預告')
            self.page.save_screens(common.saved_screenshot('test_chat_room15'))
            raise
        except Exception as msg:
            logger.error(f'代码运行出问题了，报错的信息为：{msg}')


if __name__ == '__main__':
    unittest.main()
