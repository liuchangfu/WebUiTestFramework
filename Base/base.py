# _*_ coding:utf-8 _*_
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from framework import common


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
            element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(loc))
            return element
        except NoSuchElementException:
            logger.info(f'{self}页面未能找到{loc}元素')

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
    def run_script(self, n=1000):
        js = "var q=document.documentElement.scrollTop=%d" % n
        logger.info('正在执行下拉操作(默认为下拉1000个象素).')
        self.driver.execute_script(js)

    # 重定义send_keys()方法
    def send_keys(self, loc, value):
        try:
            self.driver.find_element(*loc).clear()
            self.driver.find_element(*loc).send_keys(value)
        except Exception:
            logger.info(f'输入{value}失败!!!')

    # 重定义click()方法
    def click(self, *loc):
        try:
            self.driver.find_element(*loc).click()
        except NoSuchElementException:
            logger.info('页面元素不存在：{}', *loc)

    # 显式等待,time的单位为秒
    def imp_wait(self, time):
        self.driver.implicitly_wait(time)

    # 获取当前页面title
    def get_title(self):
        return self.driver.title

    # 隐式等待
    def wait(self, title):
        try:
            WebDriverWait(self.driver, 5).until(EC.title_contains(title))
        except Exception as msg:
            logger.info(f'未获取到网页标题:{msg}')

    # 获取网页源代码
    def get_page_source(self):
        return self.driver.page_source.encode("utf-8")

    # 截图方法
    def save_screens(self, directory):
        try:
            return self.driver.save_screenshot(directory)
        except Exception as msg:
            logger.info(f'截图失败:{msg}')

    # 切换到当前窗口
    def switch_to_window(self):
        try:
            windows = self.driver.window_handles
            logger.info(f'浏览器打开所有的窗口:{windows}')
            cur_windows = windows[-1]
            logger.info(f'当前窗口为:{cur_windows}')
            self.driver.switch_to.window(cur_windows)
        except NoSuchWindowException:
            logger.info('切换窗口失败！！', )

    # 获取输入框中的文本值
    def get_text(self, *loc):
        try:
            text = self.driver.find_element(*loc).text
            logger.info(f'获取的文本值为:{text}')
            return text
        except NoSuchElementException:
            logger.info('页面元素不存在，获取文本信息失败：{*loc}')

    # 增加cookies
    def add_cookies(self):
        dict1 = common.get_yaml_config_file('config.yaml')
        cookies1 = {
            'name': dict1['COOKES'][0]['NAME1'],
            'value': dict1['COOKES'][0]['VAULE1'],
            'domain': dict1['COOKES'][2]['DOMAIN'],
            'path': '/',
            'httpOnly': True,
            'secure': False
        }

        cookies2 = {
            'name': dict1['COOKES'][1]['NAME2'],
            'value': dict1['COOKES'][1]['VAULE2'],
            'domain': dict1['COOKES'][2]['DOMAIN'],
            'path': '/',
            'httpOnly': True,
            'secure': False
        }
        self.driver.add_cookie(cookies1)
        self.driver.add_cookie(cookies2)
        self.driver.refresh()
