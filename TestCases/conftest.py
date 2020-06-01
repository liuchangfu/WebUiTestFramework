# _*_ coding:utf-8 _*_
# author:Administrator
# datetime:2020/4/28 16:20

import pytest
from Base.baidupage import BaiDuSearchPage
from Base.PageObject.HomePage import HomePage
from Base.PageObject.LotteryPage import LotteryPage
from framework.common import saved_log
from loguru import logger


@pytest.fixture(scope='module')
def create_log(request):
    log_name = request.param
    logger.add(saved_log(log_name), format="{time:YYYY-MM-DD----HH:mm:ss}--{level}--{message}",
               rotation='10 MB',
               encoding='utf-8',
               retention='5 days'
               )


@pytest.fixture(scope='class')
def init_pages(driver):
    baidu_page = BaiDuSearchPage(driver)
    home_page = HomePage(driver)
    lottery_page = LotteryPage(driver)
    yield driver, baidu_page, home_page, lottery_page

# @pytest.fixture(scope='function')
# def open_url(init_pages):
#     driver = init_pages[0]
#     # baidu_page = init_pages[1]
#     # home_page = init_pages[2]
#     yield driver
