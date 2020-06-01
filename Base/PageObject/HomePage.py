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
    # 百家乐房间
    loc5 = (By.XPATH, home_nav_loc[3])
    # 秀场百家乐房间
    loc6 = (By.XPATH, home_nav_loc[4])
    # 鱼虾蟹房间
    loc7 = (By.XPATH, home_nav_loc[5])
    # 竞猜中心
    loc8 = (By.XPATH, home_nav_loc[7])
    # 彩票大厅
    loc9 = (By.XPATH, home_nav_loc[8])
    # 热贴推荐
    loc10 = (By.XPATH, "//div[@class='cb-hotPostsB']//a[@class='cb-titleB']")
    # 热贴中的头条摘要信息
    loc11 = (By.XPATH, "//div[@class='detailsB']//div")
    # 查看详情
    loc12 = (By.XPATH, "//span[@class='more']")
    # 头条标题
    loc13 = (By.XPATH, "//a[contains(text(),'.....')]")
    # 个人房间
    loc14 = (By.XPATH, "//div[@class='cb-privateRoomB']//a[@class='cb-titleB']")
    # 个人房间名称
    loc15 = (By.XPATH,
             "//body/div[@id='app']/div[@class='kxlive-indexPage']/div[@class='pub-main-container']/div["
             "@class='index-community']/div[@class='ip-communityBlock']/div[@class='cb-privateRoomB']/div["
             "@class='privateRoomB']/ul/li[1]/div[1]/a[1]")

    # toast提示
    loc16 = (By.XPATH, "//div[@class='toastB']")

    # 房间开播状态标签
    loc17 = (By.XPATH,
             "//body/div[@id='app']/div[@class='kxlive-indexPage']/div[@class='pub-main-container']/div["
             "@class='index-community']/div[@class='ip-communityBlock']/div[@class='cb-privateRoomB']/div["
             "@class='privateRoomB']/ul/li[1]/div[1]/span[1]")

    # 房主
    loc18 = (By.XPATH, "//div[@class='index-community']//li[1]//div[1]//div[1]//a[1]")

    # 个人主页昵称定位
    loc19 = (By.XPATH, "//span[@class='name-text']")

    # 主播头像
    loc20 = (By.XPATH,
             "//body/div[@id='app']/div[@class='kxlive-indexPage']/div[@class='pub-main-container']/div["
             "@class='all-host']/div[@class='ip-allHostBlock']/div[@class='allHostBlock']/ul/li[1]/a[1]/img[1]")

    # 主播头像中的开播彩种名称
    loc21 = (By.XPATH,
             "//body/div[@id='app']/div[@class='kxlive-indexPage']/div[@class='pub-main-container']/div["
             "@class='all-host']/div[@class='ip-allHostBlock']/div[@class='allHostBlock']/ul/li[1]/a[1]/span[1]")

    # 主播昵称
    loc23 = (By.XPATH, "//li[1]//div[1]//a[1]//span[2]")

    # 全部主播-关注
    loc24 = (By.XPATH,
             "//body/div[@id='app']/div[@class='kxlive-indexPage']/div[@class='pub-main-container']/div["
             "@class='all-host']/div[@class='ip-allHostBlock']/div[@class='allHostBlock']/ul/li[1]/div[1]/span[1]")

    # 登录对话框，马上登录定位
    loc25 = (By.XPATH, "//div[@class='loginByPw']//span[@class='loginBtn']")

    # 显示或隐藏主播中的列表的数据
    loc26 = (By.XPATH, "//span[@class='text2']")

    #
    loc27 = (By.XPATH, "//div[@class='ahb-page']")

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

    # 点击百家乐房间
    def click_link_loc5(self):
        self.click(*self.loc5)

    # 点击百家乐房间
    def click_link_loc6(self):
        self.click(*self.loc6)

    # 点击鱼虾蟹房间
    def click_link_loc7(self):
        self.click(*self.loc7)

    # 竞猜中心
    def click_link_loc8(self):
        self.click(*self.loc8)

    # 彩票大厅
    def click_link_loc9(self):
        self.click(*self.loc9)

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
        self.sleep(5)
        title = self.get_title()
        # self.close_curr_windows()
        return title

    # 北京赛车
    def click_link_action_loc3(self):
        self.open_url()
        self.click_link_loc3()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(5)
        return self.get_title()

    # 重庆时时彩
    def click_link_action_loc4(self):
        self.open_url()
        self.click_link_loc4()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(5)
        return self.get_title()

    # 百家乐
    def click_link_action_loc5(self):
        self.open_url()
        self.click_link_loc5()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(5)
        return self.get_title()

    # 秀场百家乐
    def click_link_action_loc6(self):
        self.open_url()
        self.click_link_loc6()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(5)
        return self.get_title()

    # 鱼虾蟹
    def click_link_action_loc7(self):
        self.open_url()
        self.click_link_loc7()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(5)
        return self.get_title()

    # 竞猜中心
    def click_link_action_loc8(self):
        self.open_url()
        self.click_link_loc8()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(5)
        return self.get_title()

    # 彩票大厅
    def click_link_action_loc9(self):
        self.open_url()
        self.click_link_loc9()
        self.sleep(3)
        self.switch_to_window()
        self.sleep(5)
        return self.get_title()

    # 点击热贴推荐链接
    def click_hot_tie(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        self.sleep(5)
        self.click(*self.loc10)
        self.switch_to_window()
        soucre = self.get_source()
        self.sleep(5)
        return soucre

    # 点击热贴中的头条摘要信息
    def click_hot_text(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        self.sleep(5)
        self.click(*self.loc11)
        self.switch_to_window()
        soucre = self.get_source()
        self.sleep(5)
        return soucre

    # 点击查看详情
    def click_hot_more(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        self.sleep(5)
        self.click(*self.loc12)
        self.switch_to_window()
        soucre = self.get_source()
        self.sleep(5)
        return soucre

    # 点击头条中的标题
    def click_hot_title(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        self.sleep(5)
        self.click(*self.loc13)
        self.switch_to_window()
        soucre = self.get_source()
        self.sleep(5)
        return soucre

    # 点击个人房间
    def click__private_room(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        self.sleep(5)
        self.click(*self.loc14)
        self.switch_to_window()
        soucre = self.get_source()
        self.sleep(5)
        return soucre

    # 点击个人房间名称
    def click_private_room_self(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        self.click(*self.loc15)
        toast = self.get_element_text(*self.loc16)
        return toast

    # 点击房间状态标签
    def click_room_label(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        self.click(*self.loc17)
        toast = self.get_element_text(*self.loc16)
        return toast

    # 点击房主
    def click_room_owner(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        owner = self.get_element_text(*self.loc18)
        self.click(*self.loc18)
        self.switch_to_window()
        owner_1 = self.get_element_text(*self.loc19)
        return owner, owner_1

    # 点击主播头像
    def click_anchor_avator(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        nick_name = self.get_element_text(*self.loc23)
        self.click(*self.loc20)
        self.switch_to_window()
        self.sleep(3)
        nick_name_detail = self.get_element_text(*self.loc19)
        return nick_name, nick_name_detail

    # 点击主播昵称
    def click_anchor_nickname(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        nick_name = self.get_element_text(*self.loc23)
        self.click(*self.loc23)
        self.switch_to_window()
        self.sleep(3)
        nick_name_detail = self.get_element_text(*self.loc19)
        return nick_name, nick_name_detail

    # 点击关注按钮
    def click_anchor_follow(self):
        self.open_url()
        self.sleep(5)
        self.run_script()
        self.click(*self.loc24)
        self.sleep(3)
        login_text = self.get_element_text(*self.loc25)
        return login_text

    # 點擊顯示更多/显示全部
    def click_show_more(self):
        self.open_url()
        self.sleep(3)
        self.run_script(1700)
        self.sleep(3)
        self.click(*self.loc27)
        self.sleep(3)
        self.run_script(6000)
        click_show_text = self.get_element_text(*self.loc27)
        return click_show_text


if __name__ == '__main__':
    pass
