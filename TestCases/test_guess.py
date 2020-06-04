# -*- coding:utf-8 -*-
# @Time : 2020/6/2 12:23
# @Author : Administrator
# @File : test_guess.py
# @Software: PyCharm
# @Motto: good good study,day day up


import pytest
from loguru import logger


@pytest.mark.parametrize('create_log', ['test_guess_log'], indirect=True)
class TestGuess:

    @pytest.mark.skip(reason='跳过')
    def test_guess_01(self, create_log, init_pages):
        """验证勾选冠军位置,竞猜表格数据能否正常显示"""
        global result
        logger.info('验证勾选冠军位置,竞猜表格数据能否正常显示')
        try:
            guess_page = init_pages[4]
            result = guess_page.guess_no1()
            assert '冠軍' in result[1]
            logger.info(f'实际结果：冠軍包含在{result[1]},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：冠軍不包含在{result[1]},断言失败!!!')

    @pytest.mark.skip(reason='跳过')
    def test_guess_02(self, create_log, init_pages):
        """验证勾选收费,竞猜表格数据能否正常显示"""
        global result
        logger.info('验证勾选收费,竞猜表格数据能否正常显示')
        try:
            guess_page = init_pages[4]
            result = guess_page.guess_charge_01()
            assert '彩幣' in result
            logger.info(f'实际结果：彩幣包含在{result},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：彩幣不包含在{result},断言失败!!!')

    @pytest.mark.skip(reason='跳过')
    def test_guess_03(self, create_log, init_pages):
        """验证勾选免费,竞猜表格数据能否正常显示"""
        global result
        logger.info('验证勾选免费,竞猜表格数据能否正常显示')
        try:
            guess_page = init_pages[4]
            result = guess_page.guess_charge_02()
            assert '彩幣' not in result
            logger.info(f'实际结果：彩幣不包含在{result},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：彩幣包含在{result},断言失败!!!')

    @pytest.mark.skip(reason='跳过')
    @pytest.mark.parametrize('keyword,expected', [('', '至少輸入2個關鍵字'),
                                                  ('测', '至少輸入2個關鍵字'),
                                                  ('   ', '至少輸入2個關鍵字'),
                                                  ])
    def test_guess_04(self, create_log, init_pages, keyword, expected):
        """验证搜索关键字长度不足两个时，搜索功能是否正常"""
        global result
        logger.info('验证搜索关键字长度不足两个时，搜索功能是否正常')
        try:
            guess_page = init_pages[4]
            result = guess_page.search_1(keyword)
            assert expected in result
            logger.info(f'实际结果：{expected},预期结果：{result},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{expected},预期结果：{result},断言失败!!!')

    @pytest.mark.parametrize('keyword', ['测试', 'abc'])
    @pytest.mark.skip(reason='跳过')
    def test_guess_05(self, create_log, init_pages, keyword):
        """验证输入两个或两个以上的关键字，搜索功能是否正常"""
        global result
        logger.info('验证输入两个或两个以上的关键字，搜索功能是否正常')
        try:
            guess_page = init_pages[4]
            result = guess_page.search_2(keyword)
            assert keyword in result
            logger.info(f'实际结果：{keyword},预期结果：{result},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{keyword},预期结果：{result},断言失败!!!')

    @pytest.mark.parametrize('keyword,expected', [('测试120', '無相關用戶，換個搜索詞試試'),
                                                  ('！@￥！！！！', '無相關用戶，換個搜索詞試試'),
                                                  ])
    @pytest.mark.skip(reason='跳过')
    def test_guess_06(self, create_log, init_pages, keyword, expected):
        """验证查询不存在的的关键字，搜索功能是否正常"""
        global result
        logger.info('验证查询不存在的的关键字，搜索功能是否正常')
        try:
            guess_page = init_pages[4]
            result = guess_page.search_3(keyword)
            assert result == expected
            logger.info(f'实际结果：{result},预期结果：{expected},测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result},预期结果：{expected},断言失败!!!')

    @pytest.mark.skip(reason='跳过')
    def test_guess_07(self, create_log, init_pages):
        """验证竞猜是否能正常发布"""
        global result
        logger.info('验证竞猜是否能正常发布')
        try:
            guess_page = init_pages[4]
            result = guess_page.new_guess()
            assert result == '發佈成功'
            logger.info(f'实际结果：{result},预期结果：發佈成功,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result},预期结果：發佈成功,断言失败!!!')

    @pytest.mark.skip(reason='跳过')
    def test_guess_08(self, create_log, init_pages):
        """验证竞猜发布之后，还能否正常发布竞猜"""
        global result
        logger.info('验证竞猜发布之后，还能否正常发布竞猜')
        try:
            guess_page = init_pages[4]
            result = guess_page.new_guess_01()
            assert result == '本期已發'
            logger.info(f'实际结果：{result},预期结果：本期已發,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result},预期结果：本期已發,断言失败!!!')

    @pytest.mark.skip(reason='跳过')
    def test_guess_09(self, create_log, init_pages):
        """验证查看竞猜收费"""
        global result
        logger.info('验证查看竞猜收费')
        try:
            guess_page = init_pages[4]
            result = guess_page.pay_guess()
            assert result == '付費查看'
            logger.info(f'实际结果：{result},预期结果：付費查看,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result},预期结果：付費查看,断言失败!!!')

    def test_guess_10(self, create_log, init_pages):
        """验证余额不足时，能正常弹出充值弹窗"""
        global result
        logger.info('验证余额不足时，能正常弹出充值弹窗')
        try:
            guess_page = init_pages[4]
            result = guess_page.pay_guess_windows()
            assert '彩幣不足，請充值。' in result
            logger.info(f'实际结果：{result},预期结果：彩幣不足，請充值。测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result},预期结果：彩幣不足，請充值。断言失败!!!')


if __name__ == '__main__':
    pytest.main(['-v', 'test_guess.py'])
