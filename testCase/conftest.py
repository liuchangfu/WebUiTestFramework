# _*_ coding:utf-8 _*_
# author:Administrator
# datetime:2020/4/28 16:20

import pytest
from Base.baidupage import BaiDuSearchPage


@pytest.fixture(scope='class')
def init_pages(driver):
    baidu_page = BaiDuSearchPage(driver)
    yield driver, baidu_page


@pytest.fixture(scope='function')
def open_url(init_pages):
    driver = init_pages[0]
    baidu_page = init_pages[1]
    yield baidu_page
