# -*- coding:utf-8 -*-
# @Time : 2020/6/1 17:33
# @Author : Administrator
# @File : GuessPage.py
# @Software: PyCharm
# @Motto: good good study,day day up


from Base.BasePage import BasePage
from loguru import logger
from selenium.webdriver.common.by import By
from config.conf import GUESS_URL


class GuessPage(BasePage):
    # 位置玩法清空按钮
    loc1 = (By.XPATH, "//span[13]")
    # 位置玩法全选按钮
    loc2 = (By.XPATH, " //span[12]")
    # 冠军位置
    loc3 = (By.XPATH, "//div[@class='lotteryPublic_GuessBtn']//span[1]")
    # 竞猜数据
    loc4 = (By.XPATH, "//div[@id='guessTable']")
    #  免费
    loc5 = (By.XPATH, "//div[@class='charge']//div[1]")
    # 收费
    loc6 = (By.XPATH, "//div[@class='charge']//div[2]")
    # 查阅
    loc7 = (By.XPATH, "//tr[1]//td[5]//div[1]//span[2]")
    # 搜索结果
    loc8 = (By.XPATH, "//ul[@class='searchCard']")
    # 搜索框
    loc9 = (By.XPATH, "//input[@id='searchText']")
    # 搜索按钮
    loc10 = (By.XPATH, "//span[@id='searchIcon']")
    # 搜索提示  至少輸入2個關鍵字
    loc11 = (By.XPATH, "//div[@class='searchTips']")
    # 搜索提示
    loc12 = (By.XPATH, "//p[@class='tips']")
    # 发布竞猜按钮
    loc13 = (By.XPATH, "//span[@class='newG_btn graA']")
    # 冠亚和位置--大
    loc14 = (By.XPATH, "//ul[@class='bytes']//li[1]")
    # 冠亚和位置--单
    loc15 = (By.XPATH, "//ul[@class='oddEven']//li[1]")
    # 提交按钮
    loc16 = (By.XPATH, "//button[@id='subtable']")
    # 发布成功提示
    loc17 = (By.XPATH, "//p[@class='rs_con']")
    # 本期已發
    loc18 = (By.XPATH, "//span[@class='newG_btn graB']")
    # 查阅按钮
    loc19 = (By.XPATH, "//tr[1]//td[5]//div[1]//span[2]")
    # 付費查看按钮
    loc20 = (By.XPATH, "//div[@class='btn']")
    # 余额弹窗中的充值按钮
    loc21 = (By.XPATH, "//span[@class='next toLogin login_suer']")
    # 彩幣不足，請充值。
    loc22 = (By.XPATH, "//p[@class='c_pay']")

    #  打开竞猜首页
    def open_url(self):
        return self.load_url(GUESS_URL)

    # 点击冠军位置
    def guess_no1(self):
        self.open_url()
        self.sleep(3)
        self.click(*self.loc1)
        self.sleep(3)
        self.click(*self.loc3)
        self.sleep(3)
        text1 = self.get_element_text(*self.loc3)
        text2 = self.find_element(*self.loc4).get_attribute('innerText')
        return text1, text2

    # 收费
    def guess_charge_01(self):
        self.open_url()
        self.sleep(3)
        self.click(*self.loc5)
        self.sleep(3)
        text = self.find_element(*self.loc4).get_attribute('innerText')
        return text

    # 免费
    def guess_charge_02(self):
        self.open_url()
        self.sleep(3)
        self.click(*self.loc5)
        self.sleep(3)
        self.click(*self.loc6)
        self.sleep(3)
        text = self.find_element(*self.loc4).get_attribute('innerText')
        return text

    # 搜索关键词少于2个
    def search_1(self, keyword):
        self.open_url()
        self.sleep(3)
        self.send_keys(*self.loc9, keyword)
        self.click(*self.loc10)
        text = self.find_element(*self.loc11).get_attribute('innerText')
        self.sleep(3)
        return text

    # 搜索关键词等于2个
    def search_2(self, keyword):
        self.open_url()
        self.sleep(3)
        self.send_keys(*self.loc9, keyword)
        self.click(*self.loc10)
        text = self.find_element(*self.loc8).get_attribute('innerText')
        self.sleep(3)
        return text

    # 输入不存在的关键词
    def search_3(self, keyword):
        self.open_url()
        self.sleep(3)
        self.send_keys(*self.loc9, keyword)
        self.click(*self.loc10)
        text = self.get_element_text(*self.loc12)
        self.sleep(3)
        return text

    # 发布竞猜
    def new_guess(self):
        self.open_url()
        self.sleep(3)
        self.add_cookies()
        self.click(*self.loc13)
        self.click(*self.loc14)
        self.click(*self.loc15)
        self.click(*self.loc16)
        self.sleep(3)
        return self.get_element_text(*self.loc17)

    # 本期已發
    def new_guess_01(self):
        self.open_url()
        self.add_cookies()
        self.sleep(3)
        return self.get_element_text(*self.loc18)

    # 查看收费竞猜
    def pay_guess(self):
        self.open_url()
        self.sleep(3)
        self.add_cookies()
        self.click(*self.loc5)
        self.sleep(3)
        self.click(*self.loc19)
        self.sleep(1)
        return self.get_element_text(*self.loc20)

    # 查看收费竞猜余额
    def pay_guess_windows(self):
        self.open_url()
        self.sleep(3)
        self.add_cookies()
        self.click(*self.loc5)
        self.sleep(3)
        self.click(*self.loc19)
        self.sleep(1)
        self.click(*self.loc20)
        self.sleep(1)
        return self.get_element_text(*self.loc22)
