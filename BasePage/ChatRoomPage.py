# _*_ coding:utf-8 _*_
from BasePage.Base import BasePage
from selenium.webdriver.common.by import By


class ChatRoomPage(BasePage):

    loc_click = (By.XPATH, "//div[@class='ip-oneBlock']//li[2]//a[1]")
    loc_text = (By.XPATH, "//div[@class='editor-content no-login']")

    # 进入首页后，点击幸运飞艇房间链接
    def switch_click(self):
        self.click(*self.loc_click)

    # 切换到聊天室窗口
    def switch_handler(self):
        self.switch_to_window()

    # 获取聊天室发言输入框，默认文本信息
    def input_text(self):
        return self.get_input_text(*self.loc_text)
