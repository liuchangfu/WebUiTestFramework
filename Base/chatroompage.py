# _*_ coding:utf-8 _*_
from Base.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from loguru import logger


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
    # 弹出提示信息的定位器
    loc_text2 = (By.XPATH, "//div[@class='toast']")
    # 登录对话框，马上登录按钮定位器
    loc_text4 = (By.XPATH, "//div[@class='loginByPw']//span[@class='loginBtn']")
    # 只看关注定位器
    loc5 = (By.XPATH, "//div[@class='say-bar']//span[1]")
    # 在线用户列表，第一个用户定位器
    loc6 = (By.XPATH, "//li[4]//div[1]//div[2]//div[1]")
    # 我的关注列表定位器
    loc7 = (By.XPATH, "//div[@class='room-right-bottom-info']//nav[@class='pubHeader_select']//li[3")
    # 主播推荐，第一个主播定位器
    loc8 = (By.XPATH, "//div[@class='chat-anchor-list']//div[1]//div[1]//span[2]")
    # 关闭登录弹窗定位器
    loc9 = (By.XPATH, "//span[@class='loginClose']")
    # 聊天室输入信息文本框定位器
    loc10 = (By.XPATH, "//div[@class='editor-content']")
    # 聊天信息显示区域定位器
    loc11 = (By.XPATH, "//div[@class='chat-content-container']")
    # 夜间模式定位器
    loc12 = (By.XPATH, "//div[@class='chat-editor-container']//span[2]")
    # 夜间模式类名定位
    loc13 = (By.XPATH, "//body[@class='chat night-skin']")
    # 聊天信息区，用户头像定位
    loc14 = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div/div[22]/div[1]/img')
    # 聊天信息区,弹出提示信息的定位器
    loc15 = (By.XPATH, "//div[@class='toastB']")

    # 输入聊天信息
    def type_chat_msg(self):
        self.send_keys(*self.loc_click3)

    # 点击发送按钮
    def click_send_btn(self):
        self.click(*self.loc_click2)

    # 获取登录对话中马上登录按钮文本信息
    def get_login_text(self):
        text = self.get_text(*self.loc_text4)
        self.imp_wait(3)
        self.click(*self.loc9)
        return text

    # 获取聊天信息输入框中的默认文本
    def get_chat_msg(self):
        text = self.get_text(*self.loc_text1)
        return text

    # 点击发送按钮，弹出提示toast信息
    def click_send_btn_is_displayed(self):
        try:
            self.click(*self.loc_click2)
            self.imp_wait(3)
            toast = self.find_element(*self.loc_text2).is_displayed()
            return toast
        except NoSuchElementException:
            logger.info('没有找到该元素.....')
            return False

    # 点击聊天信息输入框中的登录链接，获取登录框中的马上登录按钮文本信息
    def click_login_link(self):
        self.click(*self.loc_click3)
        return self.get_login_text()

    # 点击只看关注按钮
    def click_follow_btn(self):
        try:
            self.click(*self.loc5)
            self.imp_wait(3)
            toast = self.find_element(*self.loc5).is_displayed()
            return toast
        except NoSuchElementException:
            logger.info('没有找到该元素.....')
            return False

    # 点击夜间模式
    def click_night_btn(self):
        self.click(*self.loc12)
        self.imp_wait(3)
        value = self.find_element(*self.loc13).get_attribute('class')
        return value

    def click_avatar(self):
        try:
            self.click(*self.loc14)
            self.imp_wait(3)
            toast = self.find_element(*self.loc15).is_displayed()
            return toast
        except NoSuchElementException:
            logger.info('没有找到该元素.....')
            return False

    # 点击主播推荐中的关注按钮
    def anchor_follow_btn(self):
        try:
            self.run_script()
            self.imp_wait(3)
            self.click(*self.loc8)
            return self.get_login_text()
        except NoSuchElementException:
            logger.info('没有找到该元素.....')
            return False

    # 点击在线用户列表中的关注按钮
    def click_online_user_btn(self):
        try:
            self.click(*self.loc6)
            return self.get_login_text()
        except NoSuchElementException:
            logger.info('没有找到该元素.....')
            return False

    # 点击我的关注链接
    def click_my_focus_link(self):
        self.click(*self.loc7)
        return self.get_login_text()
