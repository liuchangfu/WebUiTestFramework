# _*_ coding:utf-8 _*_
import time
import pytest
from loguru import logger
# from framework.myunit_baidu_pytest import StartEnd
# from Base.baidupage import BaiDuSearch


# class TestSerach(StartEnd):
#     @pytest.mark.parametrize('text,expected_text',
#                              [('selenium', 'selenium_百度搜索'),
#                               ('java', 'java_百度搜索'),
#                               ('php', 'php1_百度搜索')])
#     def test_serach(self, text, expected_text):
#         page = BaiDuSearch(self.driver)
#         logger.info(f'正在打开:{self.url}')
#         page.load_url('https://www.baidu.com')
#         logger.info(f'正在输入查询关键词:{text}')
#         page.baidu_search_action(text)
#         time.sleep(3)
#         logger.info(f'当前标题为：{page.get_title()}')
#         # assert text in baidu_page.get_title()
#         assert text + '_百度搜索' == expected_text


class TestSerach():
    @pytest.mark.parametrize('text,expected_text',
                             [('selenium', 'selenium_百度搜索'),
                              ('java', 'java_百度搜索'),
                              ('php', 'php1_百度搜索')])
    def test_serach(self, open_url, text, expected_text):
        baidu_page = open_url
        baidu_page.baidu_search_action(text)
        logger.info(f'正在输入查询关键词:{text}')
        time.sleep(3)
        logger.info(f'当前标题为：{baidu_page.get_title()}')
        # assert text in baidu_page.get_title()
        assert text + '_百度搜索' == expected_text


if __name__ == '__main__':
    pytest.main()
