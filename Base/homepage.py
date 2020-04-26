# _*_ coding:utf-8 _*_
from Base.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from loguru import logger
from framework import common


class HomePage(BasePage):
        """
        封装首页相关的操作步骤
        """
