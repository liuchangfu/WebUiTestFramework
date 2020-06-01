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
    @pytest.mark.skip(reason='跳过')
    @logger.catch
    def test_home_loc2(self, create_log, init_pages, respect_title):
        """验证幸运飞艇房间能否打开"""
        logger.info('验证幸运飞艇房间能否打开')
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc2()
            assert title == respect_title
            logger.info(f'实际结果：{title}---预期结果：{respect_title},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{title}---预期结果：{respect_title},断言失败!!!')

    # @pytest.mark.parametrize('create_log', ['test_home_run_log'], indirect=True)
    @pytest.mark.parametrize('respect_title', ['北京賽車-凱旋直播'])
    @pytest.mark.skip(reason='跳过')
    @logger.catch
    def test_home_loc3(self, create_log, init_pages, respect_title):
        """验证北京赛车房间能否打开"""
        logger.info('验证北京赛车房间能否打开')
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc3()
            assert title == respect_title
            logger.info(f'实际结果：{title}---预期结果：{respect_title},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{title}---预期结果：{respect_title},断言失败!!!')

    # @pytest.mark.parametrize('create_log', ['test_home_run_log'], indirect=True)
    @pytest.mark.parametrize('respect_title', ['歡樂生肖(重時)-凱旋直播'])
    @pytest.mark.skip(reason='跳过')
    @logger.catch
    def test_home_loc4(self, create_log, init_pages, respect_title):
        """验证歡樂生肖(重時)房间能否打开"""
        logger.info('验证歡樂生肖(重時)房间能否打开')
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc4()
            assert title == respect_title
            logger.info(f'实际结果：{title}---预期结果：{respect_title},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{title}---预期结果：{respect_title},断言失败!!!')

    @pytest.mark.parametrize('respect_title', ['百家乐'])
    @pytest.mark.skip(reason='跳过')
    @logger.catch
    def test_home_loc5(self, create_log, init_pages, respect_title):
        """验证百家乐房间能否打开"""
        logger.info('验证百家乐房间能否打开')
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc5()
            assert title in respect_title
            logger.info(f'实际结果：{title}包含在预期结果：{respect_title}中,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{title}不包含预期结果：{respect_title}中,断言失败!!!')

    @pytest.mark.parametrize('respect_title', ['秀场百家乐'])
    @pytest.mark.skip(reason='跳过')
    @logger.catch
    def test_home_loc6(self, create_log, init_pages, respect_title):
        """验证秀场百家乐房间能否打开"""
        logger.info('验证秀场百家乐房间能否打开')
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc6()
            assert title in respect_title
            logger.info(f'实际结果：{title}包含在预期结果：{respect_title}中,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{title}不包含预期结果：{respect_title}中,断言失败!!!')

    @pytest.mark.parametrize('respect_title', ['魚蝦蟹'])
    @pytest.mark.skip(reason='跳过')
    @logger.catch
    def test_home_loc7(self, create_log, init_pages, respect_title):
        """验证魚蝦蟹房间能否打开"""
        logger.info('验证魚蝦蟹房间能否打开')
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc7()
            assert respect_title in title
            logger.info(f'预期结果：{respect_title}包含在实际结果：{title}中,测试通过!!!')
        except AssertionError:
            logger.error(f'预期结果：{respect_title}不包含实际结果：{title}不相等,断言失败!!!')

    @pytest.mark.parametrize('respect_title', ['數字競猜中心'])
    @pytest.mark.skip(reason='跳过')
    @logger.catch
    def test_home_loc8(self, create_log, init_pages, respect_title):
        """验证競猜中心能否打开"""
        logger.info('验证競猜中心能否打开')
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc8()
            assert respect_title in title
            logger.info(f'预期结果：{respect_title}包含在实际结果：{title}中,测试通过!!!')
        except AssertionError:
            logger.error(f'预期结果：{respect_title}不包含实际结果：{title}不相等,断言失败!!!')

    @pytest.mark.parametrize('respect_title', ['開獎結果'])
    @pytest.mark.skip(reason='跳过')
    @logger.catch
    def test_home_loc9(self, create_log, init_pages, respect_title):
        """验证彩票大厅能否打开"""
        logger.info('验证彩票大厅能否打开')
        global title
        try:
            home_page = init_pages[2]
            title = home_page.click_link_action_loc9()
            assert respect_title in title
            logger.info(f'预期结果：{respect_title}包含在实际结果：{title}中,测试通过!!!')
        except AssertionError:
            logger.error(f'预期结果：{respect_title}不包含实际结果：{title}不相等,断言失败!!!')

    @logger.catch
    @pytest.mark.skip(reason='跳过')
    def test_home_loc10(self, create_log, init_pages):
        """点击熱帖推薦能否打开社区首页"""
        logger.info('点击熱帖推薦能否打开社区首页')
        try:
            home_page = init_pages[2]
            result = home_page.click_hot_tie()
            assert "熱帖榜" in result
            logger.info(f'[熱帖榜]包含在预期结果中,测试通过！')
        except AssertionError:
            logger.error('[熱帖榜]不包含在预期结果中,断言失败!!!')

    @logger.catch
    @pytest.mark.skip(reason='跳过')
    def test_home_loc11(self, create_log, init_pages):
        """点击热贴中的头条摘要信息能否打开文章详情页"""
        logger.info('点击热贴中的头条摘要信息能否打开文章详情页')
        try:
            home_page = init_pages[2]
            result = home_page.click_hot_text()
            assert "熱帖榜" in result
            logger.info(f'[熱帖榜]包含在预期结果中,测试通过！')
        except AssertionError:
            logger.error('[熱帖榜]不包含在预期结果中,断言失败!!!')

    @logger.catch
    @pytest.mark.skip(reason='跳过')
    def test_home_loc12(self, create_log, init_pages):
        """点击查看详情能否跳转到文章详情页"""
        logger.info('点击查看详情能否跳转到文章详情页')
        try:
            home_page = init_pages[2]
            result = home_page.click_hot_more()
            assert "熱帖榜" in result
            logger.info(f'[熱帖榜]包含在预期结果中,测试通过！')
        except AssertionError:
            logger.error('[熱帖榜]不包含在预期结果中,断言失败!!!')

    @logger.catch
    @pytest.mark.skip(reason='跳过')
    def test_home_loc13(self, create_log, init_pages):
        """点击头条标题能否打开文章详情页"""
        logger.info('点击头条标题能否打开文章详情页')
        try:
            home_page = init_pages[2]
            result = home_page.click_hot_title()
            assert "熱帖榜" in result
            logger.info(f'[熱帖榜]包含在预期结果中,测试通过！')
        except AssertionError:
            logger.error('[熱帖榜]不包含在预期结果中,断言失败!!!')

    @logger.catch
    @pytest.mark.skip(reason='跳过')
    def test_home_loc14(self, create_log, init_pages):
        """点击个人房间能否打开房间首页"""
        logger.info('点击个人房间能否打开房间首页')
        try:
            home_page = init_pages[2]
            result = home_page.click__private_room()
            assert "房间" in result
            logger.info(f'[房间]包含在预期结果中,测试通过！')
        except AssertionError:
            logger.error('[房间]不包含在预期结果中,断言失败!!!')

    @logger.catch
    @pytest.mark.skip(reason='跳过')
    def test_home_loc14(self, create_log, init_pages):
        """未登录，点击个人房间名称能否弹出提示"""
        logger.info('未登录，点击个人房间名称能否弹出提示')
        global result
        try:
            home_page = init_pages[2]
            result = home_page.click_private_room_self()
            assert result == '請先登錄'
            logger.info(f'[房间]包含在预期结果中,测试通过！')
        except AssertionError:
            logger.error(f'实际结果：{result}与预期结果：請先登錄,断言失败!!!')

    @logger.catch
    @pytest.mark.skip(reason='跳过')
    def test_home_loc15(self, create_log, init_pages):
        """未登录，点击个人房间状态标签能否弹出提示"""
        logger.info('未登录，点击个人房间状态标签能否弹出提示')
        global result
        try:
            home_page = init_pages[2]
            result = home_page.click_room_label()
            assert result == '請先登錄'
            logger.info(f'实际结果：{result}与预期结果：請先登錄,测试通过！')
        except AssertionError:
            logger.error(f'实际结果：{result}与预期结果：請先登錄，断言失败!!!')

    @logger.catch
    @pytest.mark.skip(reason='跳过')
    def test_home_loc16(self, create_log, init_pages):
        """未登录，点击个人房间状态标签能否弹出提示"""
        logger.info('未登录，点击个人房间状态标签能否弹出提示')
        global result
        try:
            home_page = init_pages[2]
            result = home_page.click_room_owner()
            logger.info(f'实际结果：{result[0]}')
            assert result[0] in result[1]
            logger.info(f'实际结果：{result[0]}---预期结果：{result[1]},测试通过！')
        except AssertionError:
            logger.error(f'实际结果：{result[0]}----预期结果：{result[1]},断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_home_loc17(self, create_log, init_pages):
        """点击主播头像"""
        logger.info(f'点击主播头像,能否正常跳转')
        global result
        try:
            home_page = init_pages[2]
            result = home_page.click_anchor_avator()
            assert result[0] == result[1]
            logger.info(f'实际结果：{result[0]}---预期结果：{result[1]},测试通过！')
        except AssertionError:
            logger.error(f'实际结果：{result[0]}----预期结果：{result[1]},断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_home_loc18(self, create_log, init_pages):
        """点击主播昵称"""
        logger.info(f'点击主播昵称,能否正常跳转')
        global result
        try:
            home_page = init_pages[2]
            result = home_page.click_anchor_nickname()
            assert result[0] == result[1]
            logger.info(f'实际结果：{result[0]}---预期结果：{result[1]},测试通过！')
        except AssertionError:
            logger.error(f'实际结果：{result[0]}----预期结果：{result[1]},断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_home_loc18(self, create_log, init_pages):
        """未登录，点击关注按钮能否弹出登录框"""
        logger.info(f'未登录，点击关注按钮能否弹出登录框')
        global result
        try:
            home_page = init_pages[2]
            result = home_page.click_anchor_follow()
            assert result == '馬上登錄'
            logger.info(f'实际结果：{result}---预期结果：馬上登錄,测试通过！')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：馬上登錄,断言失败!!!')

    @logger.catch()
    def test_home_loc19(self, create_log, init_pages):
        """点击显示更多是否能正常加载数据"""
        logger.info(f'点击显示更多是否能正常加载数据')
        global result
        try:
            home_page = init_pages[2]
            result = home_page.click_show_more()
            assert result == '已展示全部，點擊收起'
            logger.info(f'实际结果：{result}---预期结果：已展示全部，點擊收起,测试通过！')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：已展示全部，點擊收起,断言失败!!!')


if __name__ == '__main__':
    pytest.main(['-v', 'test_home.py'])
