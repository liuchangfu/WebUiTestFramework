# coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from framework import readConfigYaml

# 读取邮箱服务器，发件人和密码
t1 = readConfigYaml.GetYamlConfig()
print(t1['EMAIL'])
EMAIL_HOST = t1['EMAIL'][0]['EMAIL_HOST']
EMAIL_USER = t1['EMAIL'][1]['EMAIL_USER']
EMAIL_PASSWORD = t1['EMAIL'][2]['EMAIL_PASSWORD']
print('邮箱主机:%s,邮箱用户名:%s,邮箱密码为:%s' % (EMAIL_HOST, EMAIL_USER, EMAIL_PASSWORD))

# 测试报告的路径
reportPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testReports')
print(reportPath)


class SendMail(object):
    """
    发送邮件
    """

    # 该函数的作用是为了在测试报告的路径下找到最新的测试报告
    def get_report(self):
        # 列出指定目录下的所有文件和子目录
        dirs = os.listdir(reportPath)
        # 把dirs目录下的文件按照创建时间的升序排序
        dirs.sort()
        # dirs返回是列表，故通过下标去获取最新的报告
        new_report_name = dirs[-1]
        print('最新的测试报告为: {0}'.format(new_report_name))
        # 返回最新测试报告的文件名
        return new_report_name

    # 该函数的目的是为了准备发送邮件的的消息内容
    def take_messages(self):
        new_report = self.get_report()
        self.msg = MIMEMultipart()
        # 邮件的标题
        self.msg['Subject'] = '{}自动化测试报告'.format('百度搜索')
        #  邮件的发送时间
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        # 读取最新测试报告的内容
        with open(os.path.join(reportPath, new_report), 'rb') as f:
            mail_body = f.read()
        # 将测试报告的内容放在邮件的正文当中
        html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        # 将html附加在msg里
        self.msg.attach(html)
        # 将测试报告放在附件中发送
        att1 = MIMEText(mail_body, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，附件的名字就是什么
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        self.msg.attach(att1)

    # 发送邮件到目标邮箱，测试报告以附件形式发送
    def send(self):
        try:
            # 发送给一个人，也可以发送多个人
            recipients = ['shift_1220@163.com']
            self.take_messages()
            # 发送邮件的人
            self.msg['from'] = EMAIL_USER
            toaddrs = recipients
            smtp = smtplib.SMTP()
            smtp.connect(EMAIL_HOST)
            # 如果发送邮件方是qq邮箱，这里的密码为授权码，而QQ邮箱登录密码
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.sendmail(self.msg['from'], toaddrs, self.msg.as_string())
            smtp.close()
            print('邮件发送成功！！')
        except smtplib.SMTPException:
            print('邮件发送失败，请检查邮件发送配置信息！！')


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
