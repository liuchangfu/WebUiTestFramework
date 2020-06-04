# -*- coding:utf-8 -*-
# @Time : 2020/6/4 15:38
# @Author : Administrator
# @File : CommunityPage.py
# @Software: PyCharm
# @Motto: good good study,day day up

from Base.BasePage import BasePage
from loguru import logger
from selenium.webdriver.common.by import By
from config.conf import GUESS_URL


class CommunityPage(BasePage):
    # 房间tab
    loc1 = (By.XPATH, "//div[@id='app']//li[2]//a[1]")
    # 動態tab
    loc2 = (By.XPATH, "//div[@id='app']//li[3]//a[1]")
    # 标题
    loc3 = (By.XPATH, "//h3[@class='summary-title']")
