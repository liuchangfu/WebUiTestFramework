# _*_ coding:utf-8 _*_
from datetime import datetime
import os
from loguru import logger
import pathlib

# 网站地址
URL = 'https://live.kk1350.com/'

# 彩票大厅网址
LOTTERY_URL = 'http://cp.kk1350.com/'

# 竞猜大厅网址
GUESS_URL = 'https://guess.kk1350.com/'

# 项目根目录
# ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = pathlib.Path.cwd().parent

# 报告目录
# REPORT_DIR = os.path.join(ROOT_DIR, 'Reports')
REPORT_DIR = ROOT_DIR.joinpath('Reports')

# 配置文件目录
# CONF_PATH = os.path.join(ROOT_DIR, 'config')
CONF_PATH = ROOT_DIR.joinpath('config')

# 测试数据所在目录
# DATA_Path = os.path.join(ROOT_DIR, 'data')
DATA_PATH = ROOT_DIR.joinpath('data')

# 当前日期
CURRENT_DATE = datetime.now().strftime('%Y-%m-%d')

# 当前时间
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')

# 邮件配置信息
# 邮件服务器
SMTP_SERVER = 'smtp.qq.com'
# 发送者
FROM_USER = '172667104@qq.com'
# 发送者密码
FROM_PASSWORD = 'ucxcwswjqrggbgia'
# 接收者
TO_USER = ['172667104@qq.com']  # 可以同时发送给多人，追加到列表中
# 邮件标题
SUBJECT = '凯旋项目自动化测试报告'
# 邮件正文
CONTENTS = '测试报告正文'
# 报告名称
# HTML_NAME = 'testReport{}.html'.format(CURRENT_TIME)
HTML_NAME = f'{CURRENT_DATE}_{CURRENT_TIME}_testcase_report.html'

# # Cookies配置
# COOKES:
#   - NAME1 : KX_LIVE_TK
#     VAULE1: 413196efe71b4b52ac89f4c7d2ca991e
#   - NAME2 : KX_LIVE_UUID
#     VAULE2 : pc-3497046b-59da-4582-8a6f-1d5e1133526b
#   - DOMAIN : .nn722.com


# 登录Cookies配置

Cookies = [
    {
        'NAME1': 'KX_LIVE_TK',
        'VAULE1': '2201ef940a884a5c8a9cccfd29999942',
    },
    {
        'NAME2': 'KX_LIVE_UUID',
        'VAULE2': '76ffe7a2-e794-435d-bbed-537036b9f4d1',
    },
    {'DOMAIN': '.kk1350.com'}
]

# logger.info(type(Cookies))
# logger.info(Cookies[0]['NAME1'])
# logger.info(Cookies[0]['VAULE1'])
# logger.info(Cookies[2]['DOMAIN'])
# logger.info(Cookies[1]['NAME2'])
# logger.info(Cookies[1]['VAULE2'])
logger.info(Cookies[2]['DOMAIN'])

