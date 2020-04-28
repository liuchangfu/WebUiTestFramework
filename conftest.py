# _*_ coding:utf-8 _*_
# author:Administrator
# datetime:2020/4/28 15:36

import pytest
from selenium import webdriver
from loguru import logger

_driver = None


@pytest.fixture(scope='module')
def driver():
    global _driver
    logger.info('------------open browser------------')
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    yield _driver
    logger.info('------------close browser------------')
    _driver.quit()
