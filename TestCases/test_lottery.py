# -*- coding:utf-8 -*-
# @Time : 2020/5/26 18:14
# @Author : Administrator
# @File : test_lottery.py
# @Software: PyCharm
# @Motto: good good study,day day up


import pytest
from loguru import logger


@pytest.mark.parametrize('create_log', ['test_lottery_log'], indirect=True)
class TestLottery:

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_01(self, create_log, init_pages):
        """验证历史开奖页面是否能打开"""
        global result
        logger.info('验证历史开奖页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_kaijiang()
            assert result == '歷史開獎'
            logger.info(f'实际结果：{result}----预期结果：歷史開獎,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：歷史開獎,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_02(self, create_log, init_pages):
        """验证开奖视频页面是否能打开"""
        global result
        logger.info('验证开奖视频页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_shipin()
            assert result == '開獎視頻'
            logger.info(f'实际结果：{result}----预期结果：開獎視頻,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：開獎視頻,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_03(self, create_log, init_pages):
        """验证今日號碼页面是否能打开"""
        global result
        logger.info('验证今日號碼页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_opencodeanalysis()
            assert result == '今日號碼'
            logger.info(f'实际结果：{result}----预期结果：今日號碼,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：今日號碼,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_04(self, create_log, init_pages):
        """验证冷熱分析页面是否能打开"""
        global result
        logger.info('验证冷熱分析页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_coldhotnumber()
            assert result == '今日號碼'
            logger.info(f'实际结果：{result}----预期结果：冷熱分析,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：冷熱分析,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_05(self, create_log, init_pages):
        """验证特碼分析页面是否能打开"""
        global result
        logger.info('验证特碼分析页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_specialview()
            assert result == '特碼分析'
            logger.info(f'实际结果：{result}----预期结果：特碼分析,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：特碼分析,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_06(self, create_log, init_pages):
        """验证投資價值页面是否能打开"""
        global result
        logger.info('验证投資價值页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_investmentvalue()
            assert result == '投資價值'
            logger.info(f'实际结果：{result}----预期结果：投資價值,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：投資價值,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_07(self, create_log, init_pages):
        """验证號碼規律页面是否能打开"""
        global result
        logger.info('验证號碼規律页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_numberrulestat()
            assert result == '號碼規律'
            logger.info(f'实际结果：{result}----预期结果：號碼規律,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：號碼規律,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_08(self, create_log, init_pages):
        """验证開號統計页面是否能打开"""
        global result
        logger.info('验证開號統計页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_kaihaoview()
            assert result == '號碼規律'
            logger.info(f'实际结果：{result}----预期结果：開號統計,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：開號統計,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_09(self, create_log, init_pages):
        """验证冠亞和遺漏页面是否能打开"""
        global result
        logger.info('验证冠亞和遺漏页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_gyhomit()
            assert result == '冠亞和遺漏'
            logger.info(f'实际结果：{result}----预期结果：冠亞和遺漏,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：冠亞和遺漏,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_10(self, create_log, init_pages):
        """验证號碼遺漏页面是否能打开"""
        global result
        logger.info('验证冠亞和遺漏页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_yilou()
            assert result == '號碼遺漏'
            logger.info(f'实际结果：{result}----预期结果：號碼遺漏,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：號碼遺漏,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_11(self, create_log, init_pages):
        """验证歷史統計页面是否能打开"""
        global result
        logger.info('验证歷史統計页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_ballstat()
            assert result == '歷史統計'
            logger.info(f'实际结果：{result}----预期结果：歷史統計,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：歷史統計,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_12(self, create_log, init_pages):
        """验证每日長龍页面是否能打开"""
        global result
        logger.info('验证每日長龍页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_changlongdaystat()
            assert result == '每日長龍'
            logger.info(f'实际结果：{result}----预期结果：每日長龍,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：每日長龍,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_13(self, create_log, init_pages):
        """验证遺漏大數據页面是否能打开"""
        global result
        logger.info('验证遺漏大數據页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_omitdata()
            assert result == '遺漏大數據'
            logger.info(f'实际结果：{result}----预期结果：遺漏大數據,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：遺漏大數據,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_14(self, create_log, init_pages):
        """验证特殊形態統計页面是否能打开"""
        global result
        logger.info('验证特殊形態統計页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_specialformdata()
            assert result == '特殊形態統計'
            logger.info(f'实际结果：{result}----预期结果：特殊形態統計,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：特殊形態統計,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_15(self, create_log, init_pages):
        """验证號碼走位報警页面是否能打开"""
        global result
        logger.info('验证號碼走位報警页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_numpositionalarm()
            assert result == '號碼走位報警'
            logger.info(f'实际结果：{result}----预期结果：號碼走位報警,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：號碼走位報警,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_16(self, create_log, init_pages):
        """验证兩面數據統計页面是否能打开"""
        global result
        logger.info('验证兩面數據統計页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_twosidedstat()
            assert result == '兩面數據統計'
            logger.info(f'实际结果：{result}----预期结果：兩面數據統計,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：兩面數據統計,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_17(self, create_log, init_pages):
        """验证综合路珠页面是否能打开"""
        global result
        logger.info('验证综合路珠页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.clcik_luzhuanalysis()
            assert result == '綜合路珠'
            logger.info(f'实际结果：{result}----预期结果：綜合路珠,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：綜合路珠,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_18(self, create_log, init_pages):
        """验证单双大小路珠页面是否能打开"""
        global result
        logger.info('验证单双大小路珠页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_luzhubigorsmall()
            assert result == '单双大小路珠'
            logger.info(f'实际结果：{result}----预期结果：单双大小路珠,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：单双大小路珠,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_19(self, create_log, init_pages):
        """验证龙虎路珠页面是否能打开"""
        global result
        logger.info('验证龙虎路珠页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_luzhulonghu()
            assert result == '龙虎路珠'
            logger.info(f'实际结果：{result}----预期结果：龙虎路珠,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：龙虎路珠,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_20(self, create_log, init_pages):
        """验证冠亞和路珠页面是否能打开"""
        global result
        logger.info('验证冠亞和路珠页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_guanyahestat()
            assert result == '冠亞和路珠'
            logger.info(f'实际结果：{result}----预期结果：冠亞和路珠,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：冠亞和路珠,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_21(self, create_log, init_pages):
        """验证號碼前後路珠页面是否能打开"""
        global result
        logger.info('验证號碼前後路珠页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_luzhuleftorright()
            assert result == '號碼前後路珠'
            logger.info(f'实际结果：{result}----预期结果：號碼前後路珠,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：號碼前後路珠,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_22(self, create_log, init_pages):
        """验证單雙大小走勢圖页面是否能打开"""
        global result
        logger.info('验证單雙大小走勢圖页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_bsoetrend()
            assert result == '單雙大小走勢圖'
            logger.info(f'实际结果：{result}----预期结果：單雙大小走勢圖,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：單雙大小走勢圖,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_23(self, create_log, init_pages):
        """验证橫版走勢圖页面是否能打开"""
        global result
        logger.info('验证橫版走勢圖页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_zoushitu()
            assert result == '橫版走勢圖'
            logger.info(f'实际结果：{result}----预期结果：橫版走勢圖,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：橫版走勢圖,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_24(self, create_log, init_pages):
        """验证位置走勢页面是否能打开"""
        global result
        logger.info('验证位置走勢页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_positiontrend()
            assert result == '位置走勢'
            logger.info(f'实际结果：{result}----预期结果：位置走勢,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：位置走勢,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_25(self, create_log, init_pages):
        """验证號碼走勢页面是否能打开"""
        global result
        logger.info('验证號碼走勢页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_numbertrend()
            assert result == '號碼走勢'
            logger.info(f'实际结果：{result}----预期结果：號碼走勢,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：號碼走勢,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_26(self, create_log, init_pages):
        """验证號碼走勢页面是否能打开"""
        global result
        logger.info('验证號碼走勢页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_guanyatrend()
            assert result == '冠亞和走勢'
            logger.info(f'实际结果：{result}----预期结果：冠亞和走勢,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：冠亞和走勢,断言失败!!!')

    @logger.catch()
    @pytest.mark.skip(reason='跳过')
    def test_lottery_27(self, create_log, init_pages):
        """验证自選走勢页面是否能打开"""
        global result
        logger.info('验证自選走勢页面是否能打开')
        try:
            lottery_page = init_pages[3]
            result = lottery_page.click_positionanalyze()
            assert result == '自選走勢'
            logger.info(f'实际结果：{result}----预期结果：自選走勢,测试通过!!!')
        except AssertionError:
            logger.error(f'实际结果：{result}----预期结果：自選走勢,断言失败!!!')


if __name__ == '__main__':
    pytest.main(['-v', 'test_lottery.py'])
