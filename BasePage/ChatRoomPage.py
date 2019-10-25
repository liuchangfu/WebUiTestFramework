# _*_ coding:utf-8 _*_
from BasePage.Base import BasePage
from selenium.webdriver.common.by import By


class ChatRoomPage(BasePage):
    input_text = (By.XPATH, "//div[@class='editor-content no-login']")
    switch_click = (By.XPATH, "//div[@class='ip-oneBlock']//li[2]//a[1]")

    def switch_click(self):
        self.click(*self.switch_click)

    def input_text(self):
        self.get_input_text(*self.input_text)
