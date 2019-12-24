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

    def test_chatroom01(self):
        """未登录:校验聊天输入框默认显示文本"""
        try:
            logger.info('T-未登录:校验聊天输入框默认显示文本')
            self.page.wait(3)
            text1 = self.page.get_text1()
            self.assertEqual(text1, '登錄后才可以聊天哦！')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text1, '登錄后才可以聊天哦！')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            logger.error('未登录:校验聊天输入框默认显示文本，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text1, '登錄后才可以聊天哦！')
            directory = SaveScreen('未登录-聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，请检查代码！！报错的信息为：{}', msg)

    def test_chatroom2(self):
        """未登录：点击发送按钮，校验弹出提示信息"""
        try:
            logger.info('T-未登录：点击发送按钮，校验弹出提示信息')
            self.page.click2()
            self.page.wait(1)
            text2 = self.page.get_text2()
            self.assertEqual(text2, '親，需要登錄才有發言權限哦！')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text2, '親，需要登錄才有發言權限哦！')
        except AssertionError:
            logger.error('未登录：点击发送按钮，校验弹出提示信息，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text2, '親，需要登錄才有發言權限哦！')
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            directory = SaveScreen('未登录-聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，请检查代码！！报错的信息为：{}', msg)

    def test_chatroom3(self):
        """未登录:点击聊天信息输入框的登录链接，能否弹出登录对话框"""
        try:
            logger.info('T-未登录:点击聊天信息输入框的登录链接，能否弹出登录对话框')
            self.page.click3()
            text3 = self.page.get_text3()
            time.sleep(1)
            self.page.click8()
            self.assertEqual(text3, '馬上登錄')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text3, '馬上登錄')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            logger.error('未登录:点击聊天信息输入框的登录链接，能否弹出登录对话框，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text3, '馬上登錄')
            directory = SaveScreen('未登录-聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，请检查代码！！报错的信息为：{}', msg)

    def test_chatroom4(self):
        """未登录:点击只看关注，校验弹出提示信息"""
        try:
            logger.info('T-未登录:点击只看关注，校验弹出提示信息')
            self.page.click4()
            text4 = self.page.get_text4()
            self.assertEqual(text4, '請先登錄')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text4, '請先登錄')
        except AssertionError:
            logger.error('未登录:点击只看关注，校验弹出提示信息，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text4, '請先登錄')
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            directory = SaveScreen('未登录-聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，请检查代码！！报错的信息为：{}', msg)

    def test_chatroom5(self):
        """未登录：点击在线用户列表中的关注，能否弹出登录对话框"""
        try:
            logger.info('T-未登录：点击在线用户列表中的关注，能否弹出登录对话框')
            self.page.ele_loc6_wait()
            self.page.click5()
            text5 = self.page.get_text3()
            time.sleep(3)
            self.page.click8()
            self.assertEqual(text5, '馬上登錄')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text5, '馬上登錄')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            logger.error('未登录：点击在线用户列表中的关注，能否弹出登录对话框，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text5, '馬上登錄')
            directory = SaveScreen('未登录-聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，请检查代码！！报错的信息为：{}', msg)

    def test_chatroom6(self):
        """未登录：点击我的关注列表，能否弹出登录对话框"""
        try:
            logger.info('T-未登录：点击我的关注，能否弹出登录对话框')
            self.page.click6()
            self.page.wait(3)
            text6 = self.page.get_text3()
            time.sleep(3)
            self.page.click8()
            self.assertEqual(text6, '馬上登錄')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text6, '馬上登錄')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            logger.error('未登录：点击我的关注，能否弹出登录对话框，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text6, '馬上登錄')
            directory = SaveScreen('未登录-聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，请检查代码！！报错的信息为：{}', msg)

    def test_chatroom7(self):
        """未登录：点击主播推荐列表中的的关注，能否弹出登录对话框"""
        try:
            logger.info('T-未登录：点击主播推荐列表中的的关注，能否弹出登录对话框')
            self.page.wait(5)
            self.page.run_script()
            self.page.click7()
            text7 = self.page.get_text3()
            time.sleep(1)
            self.page.click8()
            self.assertEqual(text7, '馬上登錄')
            logger.success('预期结果：{},实际结果：{}，测试通过！！', text7, '馬上登錄')
        except AssertionError:
            logger.add(GetLog('Fail--断言不通过').save_path(), rotation="500 MB", encoding='utf-8',
                       level='ERROR')
            logger.error('未登录：点击主播推荐列表中的的关注，能否弹出登录对话框，预期结果:{},实际结果:{}，实际结果与预期结果不相等，断言失败！！！', text7, '馬上登錄')
            directory = SaveScreen('未登录-聊天室页面').save_screen()
            self.page.save_screens(directory)
            raise
        except Exception as msg:
            logger.error('代码运行出问题了，请检查代码！！报错的信息为：{}', msg)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
