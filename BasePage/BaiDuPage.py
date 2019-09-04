# _*_ coding:utf-8 _*_
from BasePage.Base import BasePage
from selenium.webdriver.common.by import By

"""
 以百度为例，定位百度搜索页面的操作行为，如输入查询关键字（input_username）和点击百度一下按钮（input_password）
"""


class BaiDuSerach(BasePage):
    # 定位器，通过元素属性定位元素
    serach_text = (By.ID, 'kw')
    serach_btn = (By.ID, 'su')

    # 输入搜索关键字
    def serach_text_input(self, keywords):
        self.driver.find_element(*self.serach_text).send_keys(keywords)

    # 点击百度一下按钮
    def serach_click(self):
        self.driver.find_element(*self.serach_btn).click()
