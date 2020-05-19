# _*_ coding:utf-8 _*_
# author:Administrator
# datetime:2020/4/28 14:27
import time
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)
from loguru import logger


class BasePage:
    """结合显示等待封装一些selenium内置方法"""

    def __init__(self, diver, timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.driver = diver
        self.timeout = timeout

    def find_element(self, by, locator):
        """
        find alone element
        :param by: eg: id, name, xpath, css.....
        :param locator: id, name, xpath for str
        :return: element object
        """
        try:
            logger.info(f'Starting find the element {locator} by {by}!')
            element = WD(self.driver, self.timeout).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            logger.error(f'error: found {locator} timeout!:{t}')
        else:
            return element

    def find_elements(self, by, locator):
        """
        find group elements
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: elements object
        """
        try:
            logger.info(f'start find the elements {locator} by {by}')
            elements = WD(self.driver, self.timeout).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            logger.error(f'error: found "{locator}" timeout!:{t}')
        else:
            return elements

    def is_element_exist(self, by, locator):
        """
        assert element if exist
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: if element return True else return false
        """
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.timeout). \
                    until(ec.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                logger.error(f'Error: element {locator} not exist')
                return False
            return True
        else:
            logger.info(f'the {by} error!')

    def is_click(self, by, locator):
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.timeout). \
                    until(ec.element_to_be_clickable((self.byDic[by], locator)))
            except TimeoutException:
                logger.error("元素不可以点击")
            else:
                return element
        else:
            logger.error(f'the {by} error!')

    def is_alert(self):
        """
        assert alert if exsit
        :return: alert obj
        """
        try:
            re = WD(self.driver, self.timeout).until(ec.alert_is_present())
        except (TimeoutException, NoAlertPresentException):
            logger.error("error:no found alert")
        else:
            return re

    def switch_to_frame(self, by, locator):
        """判断frame是否存在，存在就跳到frame"""
        logger.info(f'info:switching to iframe "{locator}"')
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.timeout). \
                    until(ec.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
            except TimeoutException as t:
                logger.error(f'error: found {locator} timeout！切换frame失败!:{t}')
        else:
            logger.error(f'the {by} error!')

    def switch_to_default_frame(self):
        """返回默认的frame"""
        logger.info('switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            logger.error(e)

    def get_alert_text(self):
        """获取alert的提示信息"""
        alert = self.is_alert()
        if alert:
            return alert.text
        else:
            return None

    def get_element_text(self, by, locator, name=None):
        """获取某一个元素的text信息"""
        try:
            element = self.find_element(by, locator)
            if name:
                return element.get_attribute(name)
            else:
                return element.text
        except AttributeError:
            logger.error(f'get {locator} text failed return None')

    def load_url(self, url):
        """加载url"""
        logger.info(f'string upload url {url}')
        self.driver.get(url)

    def get_source(self):
        """获取页面源码"""
        return self.driver.page_source

    def send_keys(self, by, locator, value=''):
        """写数据"""
        logger.info(f'info:input {value}')
        try:
            element = self.find_element(by, locator)
            element.send_keys(value)
        except AttributeError as e:
            logger.info(e)

    def clear(self, by, locator):
        """清理数据"""
        logger.info('info:clearing value')
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            logger.error(e)

    def click(self, by, locator):
        """点击某个元素"""
        logger.info(f'click {locator}')
        element = self.is_click(by, locator)
        if element:
            element.click()
        else:
            logger.error(f'the {locator} unclickable!')

    @staticmethod
    def sleep(num=0):
        """强制等待"""
        logger.info(f'sleep {num} minutes')
        time.sleep(num)

    def wait_element_to_be_located(self, by, locator):
        """显示等待某个元素出现，且可见"""
        logger.info(f'waiting {locator} to be located')
        try:
            return WD(self.driver, self.timeout).until(ec.presence_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            logger.error(f'found {locator} timeout！:{t}')

    def get_page_source(self):
        return self.get_source()

    # 定义run_script()方法，用于执行js脚本
    def run_script(self, n=1000):
        js = f"var q=document.documentElement.scrollTop={n}"
        logger.info('正在执行下拉操作(默认为下拉1000个象素).')
        self.driver.execute_script(js)

    # 鼠标滑动到某个位置
    def run_scroll_into_view(self, target):
        logger.info('正在执行鼠标滚轮操作.......')
        self.driver.execute_script("arguments[0].scrollIntoView(); ", target)

    # 截图方法
    def save_screens(self, directory):
        try:
            return self.driver.save_screenshot(directory)
        except Exception as msg:
            logger.error(f'截图失败:{msg}')

    # 获取当前页面title
    def get_title(self):
        return self.driver.title


if __name__ == '__main__':
    pass
