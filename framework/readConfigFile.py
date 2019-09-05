# coding=utf-8
import os
import codecs
import configparser

configPath = os.path.abspath(os.curdir) + '\\testConfig\\config.ini'
print(configPath)


class ReadConfig(object):

    # 构造函数，读取配置文件
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(configPath)

    # 从config.ini中读取url地址
    def get_http(self, name):
        value = self.config.get("HTTP", name)
        return value

    # 从config.ini中读取email地址
    def get_email(self, name):
        value = self.config.get("EMAIL", name)
        return value
