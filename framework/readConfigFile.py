# coding=utf-8
import os
import codecs
import configparser

# configPath = os.path.abspath(os.curdir) + '\\testConfig\\config.ini'
configPath = os.pardir + '\\testConfig\\config.ini'
print(configPath)


# path = os.pardir + '\\testConfig\\config.ini'
# print(path)


class ReadConfig(object):
    # 构造函数，读取配置文件，如果配置文件有中文的话， 需要在read方法中加入encoding='utf-8'参数，不然会提示UnicodeDecodeError异常
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(configPath, encoding='utf-8')

    # 从config.ini中读取url地址
    def get_http(self, name):
        value = self.config.get("HTTP", name)
        return value

    # 从config.ini中读取email配置的email的host地址
    def get_email_host(self, name):
        value = self.config.get("EMAIL", name)
        return value

    # 从config.ini中读取email配置中的用户名
    def get_email_user(self, name):
        value = self.config.get('EMAIL', name)
        return value

    # 从config.ini中读取email配置项中的密码
    def get_email_password(self, name):
        value = self.config.get('EMAIL', name)
        return value



# # 调试代码
# con = ReadConfig()
# a = con.get_http('URL')
# print(a)
#
# b = con.get_email_host('EMAIL_HOST')
# print(b)

# c = ReadConfig().get_email_password('EMAIL_PASSWORD')
# print(c)