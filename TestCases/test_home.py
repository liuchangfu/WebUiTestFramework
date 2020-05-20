# -*- coding:utf-8 -*-
# @Time : 2020/5/19 17:01
# @Author : Administrator
# @File : test_home.py
# @Software: PyCharm
# @Motto: good good study,day day up
import time
import pytest
from loguru import logger


@pytest.mark.parametrize('create_log', ['test_home_run_log'], indirect=True)
class TestHome:
    # @pytest.mark.parametrize('create_log', ['test_home_run_log'], indirect=True)
    @pytest.mark.parametrize('respect_title', ['幸運飛艇-凱旋直播'])
    def test_home_loc2(self, create_log, init_pages, respect_title):
        """验证幸运飞艇房间能否打开"""
        global title
        try:
            """验证幸运飞艇房间能否打开"""
            home_page = init_pages[2]
            title = home_page.click_link_action_loc2()
            logger.info(f'当前标题为：{title}')
            assert title == respect_title
        except AssertionError:
            logger.info(f'实际结果：{title}与预期结果：[respect_title]不相等,断言失败!!!')

    # @pytest.mark.parametrize('create_log', ['test_home_run_log'], indirect=True)
    @pytest.mark.parametrize('respect_title', ['北京賽車-凱旋直播'])
    def test_home_loc3(self, create_log, init_pages, respect_title):
        """验证北京赛车房间能否打开"""
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc3()
            logger.info(f'当前标题为：{title}')
            assert title == respect_title
        except AssertionError:
            logger.info(f'实际结果：{title}与预期结果：[respect_title]不相等,断言失败!!!')

    # @pytest.mark.parametrize('create_log', ['test_home_run_log'], indirect=True)
    @pytest.mark.parametrize('respect_title', ['歡樂生肖(重時)-凱旋直播'])
    def test_home_loc4(self, create_log, init_pages, respect_title):
        """验证重庆时时彩房间能否打开"""
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc4()
            logger.info(f'当前标题为：{title}')
            assert title == respect_title
        except AssertionError:
            logger.info(f'实际结果：{title}与预期结果：[respect_title]不相等,断言失败!!!')


if __name__ == '__main__':
    pytest.main(['-v', 'test_home.py'])
