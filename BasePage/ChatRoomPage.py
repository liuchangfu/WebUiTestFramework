# _*_ coding:utf-8 _*_
from BasePage.Base import BasePage
from selenium.webdriver.common.by import By


class ChatRoomPage(BasePage):
    """
    封装聊天室页面相关的操作步骤
    """

    # 首页中幸运飞艇聊天定位器
    loc_click1 = (By.XPATH, "//div[@class='ip-oneBlock']//li[2]//a[1]")
    # 发送按钮定位器
    loc_click2 = (By.XPATH, "//span[@class='editor-send']")
    # 聊天信息输入框中，登录链接定位器
    loc_click3 = (By.XPATH, "//div[@class='editor-content no-login']//p//span")
    # 聊天信息输入框中，默认文案定位器
    loc_text1 = (By.XPATH, "//div[@class='editor-content no-login']")
    # 弹出层的定位器
    loc_text2 = (By.XPATH, "//div[@class='toast']")
    # 登录对话框，马上登录按钮定位器
    loc_text4 = (By.XPATH, "//div[@class='loginByPw']//span[@class='loginBtn']")
    # 只看关注定位器
    loc5 = (By.XPATH, "//div[@class='say-bar']//span[1]")
    # 在线用户列表，第一个用户定位器
    loc6 = (By.XPATH, "//li[1]//div[1]//div[2]//div[1]")
    # 我的关注列表定位器
    loc7 = (By.XPATH, "//div[@class='room-right-bottom-info']//nav[@class='pubHeader_select']//li[3")
    # 主播推荐，第一个主播定位器
    loc8 = (By.XPATH, "//div[@class='chat-anchor-list']//div[1]//div[1]//span[2]")
    # 关闭登录弹窗定位器
    loc9 = (By.XPATH, "//span[@class='loginClose']")

    # 进入首页后，点击幸运飞艇房间链接
    def switch_click(self):
        self.click(*self.loc_click1)

    # 进入聊天室，点击发送按钮
    def click2(self):
        self.click(*self.loc_click2)

    # 点击聊天信息输入框的登录
    def click3(self):
        self.click(*self.loc_click3)

    # 点击只看关注
    def click4(self):
        self.click(*self.loc5)

    # 点击我的关注
    def click5(self):
        self.click(*self.loc6)

    # 点击我的关注列表
    def click6(self):
        self.click(*self.loc7)

    # 点击主播推荐列表中的关注按钮
    def click7(self):
        self.click(*self.loc8)

    # 关闭登录对话框
    def click8(self):
        self.click(*self.loc9)

    # 切换到聊天室窗口
    def switch_handler(self):
        self.switch_to_window()

    # 获取聊天室发言输入框中的默认文本信息
    def get_text1(self):
        return self.get_input_text(*self.loc_text1)

    # 点击发送按钮弹出的提示信息
    def get_text2(self):
        return self.get_input_text(*self.loc_text2)

    # 弹出登录窗口后，获取马上登录按钮文本值
    def get_text3(self):
        return self.get_input_text(*self.loc_text4)

    # 获取只看关注按钮中弹出的文本值
    def get_text4(self):
        return self.get_input_text(*self.loc_text2)

    # 加载我的关注列表娄据完后，再去点击关注按钮
    def ele_loc6_wait(self):
        self.find_element(*self.loc6)
