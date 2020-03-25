# _*_ coding:utf-8 _*_
from Base.base import BasePage
from selenium.webdriver.common.by import By


class BaiDuSearch(BasePage):
    """
     以百度搜索为例，定位百度搜索页面的操作行为，如输入查询关键字（input_username）和点击百度一下按钮（input_password）
    """

    # 定位器，通过元素属性定位元素
    type_text = (By.ID, 'kw')
    type_btn = (By.ID, 'su')

    # 输入搜索关键字
    def type_search(self, keyword):
        self.driver.find_element(*self.type_text).send_keys(keyword)

    # 点击百度一下按钮
    def btn_search(self):
        self.driver.find_element(*self.type_btn).click()

    def baidu_search_action(self, keyword):
        self.type_search(keyword)
        self.btn_search()
