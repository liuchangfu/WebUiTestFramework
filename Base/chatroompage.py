# _*_ coding:utf-8 _*_
from Base.base import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from loguru import logger
from framework import common


class ChatRoomPage(BasePage):
    """
    封装聊天室页面相关的操作步骤
    """

    # 首页中幸运飞艇聊天定位器
    loc_click1 = (By.XPATH, "//div[@class='ip-oneBlock']//li[2]//a[1]")
    # 发送按钮定位器
    loc_click2 = (By.XPATH, "//span[@class='editor-send']")
    # 未登录-聊天信息输入框中，登录链接定位器
    loc_click3 = (By.XPATH, "//div[@class='editor-content no-login']//p//span")
    # 未登录-聊天信息输入框中，默认文案定位器
    loc_text1 = (By.XPATH, "//div[@class='editor-content no-login']")
    # 弹出提示信息的定位器
    loc_text2 = (By.XPATH, "//div[@class='toast']")
    # 登录对话框，马上登录按钮定位器
    loc_text4 = (By.XPATH, "//div[@class='loginByPw']//span[@class='loginBtn']")
    # 只看关注定位器
    loc5 = (By.XPATH, "//div[@class='say-bar']//span[1]")
    # 在线用户列表，第一个用户定位器
    loc6 = (By.XPATH, "//li[4]//div[1]//div[2]//div[1]")
    # 我的关注定位器
    loc7 = (By.XPATH, "//div[@class='room-right-bottom-info']//nav[@class='pubHeader_select']//li[3]")
    # 主播推荐，第一个主播关注按钮定位器
    loc8 = (By.XPATH, "//div[@class='chat-anchor-list']//div[1]//div[1]//span[2]")
    # 关闭登录弹窗定位器
    loc9 = (By.XPATH, "//span[@class='loginClose']")
    # 聊天室输入信息文本框定位器
    loc10 = (By.XPATH, "//div[@class='editor-content']")
    # 聊天信息显示区域定位器
    loc11 = (By.XPATH, "//div[@class='chat-content-container']")
    # 夜间模式定位器
    loc12 = (By.XPATH,
             "//body[@class='chat']/div[@id='app']/div/div[@class='kxlive-room-container']/div[@class='room-container']/div[@class='room-center no-anchor']/div[@class='chat-container']/div[@class='chat-editor-container']/div[@class='say-bar']/div[@class='say-bar-left']/span[2]")
    # 夜间模式类名定位
    loc13 = (By.XPATH, "//body[@class='chat night-skin']")
    # 聊天信息区，用户头像定位
    loc14 = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div/div[22]/div[1]/img')
    # 聊天信息区,弹出提示信息的定位器
    loc15 = (By.XPATH, "//div[@class='toastB']")
    # 实时竞猜第一个用户定位器
    loc16 = (By.XPATH, "//div[@class='room-right']//tr[1]//td[1]")
    # 竞猜主页-》最新竞猜第一个用户定位器
    loc17 = (By.XPATH, '//tr[1]//td[1]//div[1]')
    # 竞猜排行定位器
    loc18 = (By.XPATH, "//div[@class='room-right-info']//li[2]")
    # 竞猜排行-连赢榜第-赢率榜-盈利榜一个用户定位器
    loc19 = (By.XPATH, "//li[1]//div[1]//div[2]//div[2]")
    # 竞猜主页-排行榜定位器
    loc20 = (By.XPATH, "//li[2]//a[1]//span[1]")
    # 竞猜主页-排行榜-連贏榜第一个用户定位器
    loc21 = (By.XPATH, "//div[@id='winning']//a[@class='name']")
    # 竞猜主页-排行榜-贏率榜(10期)第一个用户定位器
    loc22 = (By.XPATH, "//div[@id='winRate']//li[1]//a[1]")
    # 竞猜主页-排行榜-連盈利榜（10期）第一个用户定位器
    loc23 = (By.XPATH, "//div[@id='profitRate']//li[1]//a[1]")
    # 实时竞猜-赢率榜定位器
    loc24 = (By.XPATH, "//div[@class='web_mainSection']//div//li[2]")
    # 竞猜排行-赢率榜第定位器
    loc25 = (By.XPATH, "//div[@class='gue_navBlock']//li[2]")
    # 竞猜排行-盈利榜定位器
    loc26 = (By.XPATH, "//div[@class='gue_navBlock']//li[3]")
    # 主播预告定位器
    loc27 = (By.XPATH, "//div[@class='room-right-info']//li[3]")
    # 主播预告无排班提示信息定位器
    loc28 = (By.XPATH, "//p[@class='notDataBtn']")
    # 主播预告中的今天定位器
    loc29 = (By.XPATH, "//li[@class='roomPart active']//span[@class='date']")
    # 主播预告中第一位主播昵称
    loc30 = (By.XPATH, "//li[@class='roomPart active']//div[1]//a[1]//span[1]")
    # 首页幸运飞艇当前主播
    loc31 = (By.XPATH,
             "//div[@class='advanceBlock rb-xyft']//div[@class='contentB advance-content active']//li[1]//div[1]//div[1]//div[1]//span[1]//span[1]//a[1]")
    # 发言置顶
    loc32 = (By.XPATH, "//i[@class='icon-select-no']")
    # 表情定位器
    loc33 = (By.XPATH, "//i[@class='icon-emoji']")
    # 表情框中第一个表情
    loc34 = (By.XPATH, "//div[@class='chat-container']//li[1]//img[1]")
    # 我的关注列表
    loc35 = (By.XPATH, "//div[@class='myfoucs']")
    # 主播列表第一个用户的昵称
    loc36 = (By.XPATH, "//div[@class='chat-anchor-list']//div[1]//div[1]//span[1]")
    # 在线用户列表
    loc37 = (By.XPATH, "//div[@class='online']")
    # 在线用户列表第二页某个用户的关注
    loc38 = (By.XPATH, "//li[15]//div[1]//div[2]//div[1]")
    # 在线用户列表第二页某个用户的昵称
    loc39 = (By.XPATH, "//li[15]//div[1]//div[1]//div[2]//span[1]")
    # 置顶消息定位器
    loc40 = (By.XPATH, "//div[@class='chat-top-content-container']")
    # 在线用户表头定位器
    loc41 = (By.XPATH, "//div[@class='room-right-bottom-info']//li[2]")
    # 我的关注表头定位器
    loc42 = (By.XPATH, "//div[@class='room-right-bottom-info']//li[2]")

    # 输入聊天信息
    def type_chat_msg(self, text):
        self.send_keys(text, *self.loc10)

    # 点击发送按钮
    def click_send_btn(self):
        self.click(*self.loc_click2)

    # 勾上发言置顶
    def select_icon(self):
        self.click(*self.loc32)

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
            logger.error('没有找到该元素.....')
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
        logger.info(f'调试-{value}')
        return value

    # 点击头象
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

    # 获取实时竞猜第一个用户的昵称
    def guess_tab1(self):
        text = self.get_text(*self.loc16)
        return text

    # 竞猜主页-》最新竞猜第一个用户的名称
    def guess_homepage_new(self):
        logger.info('正在启动浏览器隐藏模式，请耐心等候...')
        self.driver = self.headless()
        self.url = common.get_yaml_config_file('config.yaml')['URL1'] + 'xyft/guess'
        logger.info(f'当前打开的url为:{self.url}')
        self.driver.get(self.url)
        self.imp_wait(5)
        text = self.get_text(*self.loc17)
        self.driver.quit()
        return text

    # 获取竞猜排行-连赢榜第一个用户的昵称
    def guess_tab2(self):
        self.click(*self.loc18)
        self.imp_wait(3)
        text = self.get_text(*self.loc19)
        return text

    # 竞猜主页-》排行榜連贏榜、贏率榜、盈利榜第一个用户的名称
    def guess_homepage_rank(self):
        logger.info('正在启动浏览器隐藏模式，请耐心等候...')
        self.driver = self.headless()
        self.url = common.get_yaml_config_file('config.yaml')['URL1'] + 'xyft/rank'
        logger.info(f'当前打开的url为:{self.url}')
        self.driver.get(self.url)
        self.imp_wait(5)
        text1 = self.get_text(*self.loc21)
        text2 = self.get_text(*self.loc22)
        text3 = self.get_text(*self.loc23)
        # self.driver.quit()
        return text1, text2, text3

    # 获取竞猜排行-赢率榜第一个用户的昵称
    def guess_tab2_yingyu(self):
        self.click(*self.loc18)
        self.imp_wait(3)
        self.click(*self.loc25)
        return self.get_text(*self.loc19)

    # 获取竞猜排行-盈利榜第一个用户的昵称
    def guess_tab2_yingli(self):
        self.click(*self.loc18)
        self.imp_wait(3)
        self.click(*self.loc26)
        self.imp_wait(3)
        return self.get_text(*self.loc19)

    # 主播排班中第一个主播昵称
    def chatroom_anchor_preview(self):
        self.click(*self.loc27)
        self.imp_wait(3)
        text = self.get_text(*self.loc28)
        if text == '暫無預告':
            logger.info('没有相关排班信息....')
            return text
        else:
            self.click(*self.loc27)
            self.imp_wait(3)
            return self.get_text(*self.loc30)

    # 首页主播排班中第一个主播昵称
    def homepage_anchor_preview(self):
        return self.get_text(*self.loc31)

    # 发送聊天信息
    def enter_msg_send(self, text):
        self.type_chat_msg(text)
        self.click_send_btn()
        self.imp_wait(3)
        texts = self.get_text(*self.loc11)
        if text in texts:
            return True
        else:
            return False

    # 发送表情
    def send_emoji(self):
        self.click(*self.loc33)
        self.imp_wait(2)
        self.click(*self.loc34)
        self.click(*self.loc_click2)
        texts = self.get_text(*self.loc11)
        print(texts)
        if '1f60a' in texts:
            return True
        else:
            return False

    # 主播推荐，关注第一个主播
    def chat_anchor_list(self):
        self.run_script()
        self.imp_wait(3)
        anchor = self.get_text(*self.loc36)
        if self.get_text(*self.loc8) == '關註':
            self.click(*self.loc8)
            self.imp_wait(3)
            self.click(*self.loc7)
            self.imp_wait(3)
            anchors = self.get_text(*self.loc35)
            if anchor in anchors:
                return True
            else:
                return False
        elif self.get_text(*self.loc8) == '已關註':
            self.click(*self.loc7)
            self.imp_wait(5)
            anchors = self.get_text(*self.loc35)
            if anchor in anchors:
                return True
            else:
                return False

    # 在线用户列表
    def online_user(self, nickname):
        self.click(*self.loc41)
        self.imp_wait(3)
        online_users = self.get_text(*self.loc37)
        if nickname in online_users:
            return True
        else:
            return False

    # 我的关注列表
    def check_online_user(self):
        target = self.find_element(*self.loc38)
        self.run_scrollIntoView(target)
        self.imp_wait(3)
        focus_user = self.get_text(*self.loc39)
        self.click(*self.loc38)
        self.imp_wait(3)
        self.click(*self.loc7)
        self.imp_wait(3)
        my_focus_users = self.get_text(*self.loc35)
        if focus_user in my_focus_users:
            return True
        else:
            return False

    # 输入聊天信息置顶显示
    def chat_top_msg(self, text):
        # self.imp_wait(5)
        # self.run_script(-1000)
        self.select_icon()
        self.type_chat_msg(text)
        self.click_send_btn()
        self.imp_wait(3)
        chat_top_text = self.get_text(*self.loc40)
        # chat_top_text = self.find_element(*self.loc40).is_displayed()
        return chat_top_text
