# _*_ coding:utf-8 _*_
from BasePage.Base import BasePage
from selenium.webdriver.common.by import By


class ChatRoomPage(BasePage):
    """
    封装聊天室页面相关的操作步骤
    """

    # 页面元素定位器的Xpath路径 locator
    loc_click1 = (By.XPATH, "//div[@class='ip-oneBlock']//li[2]//a[1]")
    loc_click2 = (By.XPATH, "//span[@class='editor-send']")
    loc_click3 = (By.XPATH, "//div[@class='editor-content no-login']//p//span")
    loc_text1 = (By.XPATH, "//div[@class='editor-content no-login']")
    loc_text2 = (By.XPATH, "//div[@class='toast']")
    loc_text4 = (By.XPATH, "//div[@class='loginByPw']//span[@class='loginBtn']")

    # 进入首页后，点击幸运飞艇房间链接
    def switch_click(self):
        self.click(*self.loc_click1)

    # 进入聊天室，点击发送按钮
    def click2(self):
        self.click(*self.loc_click2)

    # 点击聊天信息输入框的登录
    def click3(self):
        self.click(*self.loc_click3)

    # 切换到聊天室窗口
    def switch_handler(self):
        self.switch_to_window()

    # 获取聊天室发言输入框中的默认文本信息
    def input_text1(self):
        return self.get_input_text(*self.loc_text1)

    # 未登录，点击发送按钮弹出的提示信息
    def input_text2(self):
        return self.get_input_text(*self.loc_text2)

    # 弹出登录窗口后，获取马上登录按钮文本值
    def input_text3(self):
        return self.get_input_text(*self.loc_text4)

