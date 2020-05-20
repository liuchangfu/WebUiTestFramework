# _*_ coding:utf-8 _*_
from Base.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from loguru import logger
from framework import common
from config.conf import URL
from data.home_data import HomeData


class HomePage(BasePage):
    """
    封装首页相关的操作步骤
    """

    # 首页导航定位器
    home_nav_loc = [
        "//div[@class='ip-oneBlock']//li[1]//a[1]",
        "//div[contains(@class,'ip-oneBlock')]//li[2]//a[1]",
        "//div[contains(@class,'ip-oneBlock')]//li[3]//a[1]",
        "//div[contains(@class,'ip-oneBlock')]//li[4]//a[1]",
        "//div[contains(@class,'ip-oneBlock')]//li[5]//a[1]",
        "//div[contains(@class,'ip-oneBlock')]//li[6]//a[1]",
        "//div[contains(@class,'ip-oneBlock')]//li[7]//a[1]",
        "//div[contains(@class,'ip-oneBlock')]//li[11]//a[1]",
        "//div[contains(@class,'ip-oneBlock')]//li[12]//a[1]"
    ]

    # 飞艇公告弹窗
    loc1 = (By.XPATH, "//div[@class='kxDialog-container home-dialog']//i[@class='kxDialog-close']")
    # 幸运飞艇链接定位器
    loc2 = (By.XPATH, home_nav_loc[0])
    # 北京赛车房间定位器
    loc3 = (By.XPATH, home_nav_loc[1])
    # 重庆时时彩房间定位器
    loc4 = (By.XPATH, home_nav_loc[2])

    #  打开首页
    def open_url(self):
        return self.load_url(URL)

    # # 点击首页的头部导航
    # def click_link(self):
    #     for i in range(len(self.home_nav_loc)):
    #         self.click(*self.home_nav_loc[i])

    # 点击幸运飞艇房间
    def click_link_loc2(self):
        self.click(*self.loc2)

    # 点击北京赛车房间
    def click_link_loc3(self):
        self.click(*self.loc3)

    # 点击重庆时时彩房间
    def click_link_loc4(self):
        self.click(*self.loc4)

    # 幸运飞艇公告弹窗
    def click_dialog(self):
        try:
            self.click(*self.loc1)
        except NoSuchElementException:
            logger.info('此窗口不存在，跳过！！')

    # 幸运飞艇
    def click_link_action_loc2(self):
        self.open_url()
        self.click_dialog()
        self.click_link_loc2()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(3)
        return self.get_title()

    # 北京赛车
    def click_link_action_loc3(self):
        self.open_url()
        self.click_link_loc3()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(3)
        return self.get_title()

    # 重庆时时彩
    def click_link_action_loc4(self):
        self.open_url()
        self.click_link_loc4()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(3)
        return self.get_title()


if __name__ == '__main__':
    pass
