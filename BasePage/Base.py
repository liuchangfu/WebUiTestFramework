# _*_ coding:utf-8 _*_
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


class BasePage(object):
    """
    二次封装所有selenium api的方法，例如打开页面等
    """

    # 初始化driver,url等
    def __init__(self, driver, base_url):
        # self.driver = webdriver.Firefox()
        self.driver = driver
        self.url = base_url

    # 打开页面
    def _open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的链接地址是否与配置的地址一致，调用on_page()方法
        # assert self.on_page(page_title), '打开页面失败:%s' % url

    # 重写元素定位方法,参数传入方式为元组
    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except:
            # print('%s页面未能找到%s元素！' % (self, loc))
            logger.info('{}页面未能找到{}元素', (self, loc))

    # 重写switch_to方法
    def switch_to_frame(self, loc):
        return self.driver.switch_to(loc)

    # 定义open方法，调用_open()方法打开链接
    def open(self):
        self._open(self.url)

    # 当前窗口标题与配置地址标题进行比较
    # def on_page(self, page_title):
    #     return page_title in self.driver.title

    # 定义run_script()方法，用于执行js脚本
    def run_script(self, script):
        self.driver.execute_script(script)

    # 重定义send_keys()方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.driver.find_element(*loc).click()
            if clear_first:
                self.driver.find_element(*loc).clear()
                self.driver.find_element(*loc).send_keys(vaule)
        except AttributeError:
            # print('%s页面未能找到%元素' % (self, loc))
            logger.info('{}页面未能找到{}元素', (self, loc))

    # 重定义click()方法
    def click(self, *loc):
        try:
            self.driver.find_element(*loc).click()
        except BaseException:
            logger.info('页面元素不存在：{}', *loc)

    # 显式等待,time的单位为秒
    def wait(self, time):
        self.driver.implicitly_wait(time)

    # 获取当前页面title
    def get_title(self):
        return self.driver.title

    # 隐式等待
    def driver_wait(self, title):
        try:
            WebDriverWait(self.driver, 5).until(EC.title_contains(title))
        except BaseException as msg:
            logger.info('未获取到网页标题:{}', msg)

    # 获取网页源代码
    def get_page_source(self):
        return self.driver.page_source

    # 截图方法
    def save_screens(self, directory):
        try:
            return self.driver.save_screenshot(directory)
        except BaseException as msg:
            logger.info('截图失败:{}', msg)

    # 切换窗口
    def switch_to_window(self):
        try:
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
        except BaseException:
            logger.info('切换窗口失败！！', )

    # 获取输入框中的文本值
    def get_input_text(self, *loc):
        try:
            return self.driver.find_element(*loc).text
        except BaseException:
            logger.info('页面元素不存在，获取文本信息失败：{}', *loc)
