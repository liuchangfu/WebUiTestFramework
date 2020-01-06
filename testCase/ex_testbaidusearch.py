# _*_ coding:utf-8 _*_
from framework import common
from Base.baidupage import BaiDuSearch
from ddt import ddt, unpack, data
import time
from loguru import logger
from framework.myunit1 import StartEnd
import unittest


@ddt
class TestBaiDuSearch(StartEnd):
    """
    测试类方法，该类必继承unittest.TestCase类
    """

    @data(['seleniun', 'selenium_百度搜索'], ['java', 'java_百度搜索'], ['php', 'php_百度搜索'])
    @unpack
    # 测试用例，输入搜索关键词，最后加入断言
    def test_search(self, keyword, result):
        """百度搜索测试"""
        try:
            logger.info('百度页面搜索页面，测试开始....')
            page = BaiDuSearch(self.driver, self.url)
            logger.info('输入查询关键词：{}', keyword)
            page.baidu_search_action(keyword)
            page.wait(keyword)
            time.sleep(3)
            self.assertEqual(page.get_title(), result)
            logger.success('T-百度搜索测试，预期结果:{},实际结果:{},测试通过。', keyword, result)
        except AssertionError:
            logger.add(common.saved_log('F-百度搜索测试'), encoding='utf-8',
                       level='ERROR')
            logger.error('百度搜索测试，预期结果:{},实际结果:{}，实际结果与预期结不相等，断言失败！！！', keyword, result)
            page.save_screens(common.saved_screenshot('S-百度搜索测试'))
            raise


if __name__ == '__main__':
    unittest.main()
