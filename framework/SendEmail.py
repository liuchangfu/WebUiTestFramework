# coding:utf-8

import os, sys
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 测试报告的路径
reportPath = os.path.join(os.getcwd(), 'testReports')

print(reportPath)


class SendMail(object):
    """
    发送邮件
    """

    # 该函数的作用是为了在测试报告的路径下找到最新的测试报告
    def get_report(self):
        dirs = os.listdir(reportPath)
        dirs.sort()
        new_report_name = dirs[-1]
        print('The new report name: {0}'.format(new_report_name))
        return new_report_name  # 返回的是测试报告的名字

    # 该函数的目的是为了准备发送邮件的的消息内容
    def take_messages(self):
        new_report = self.get_report()
        self.msg = MIMEMultipart()
        # 邮件的标题
        self.msg['Subject'] = 'XXX接口自动化测试报告'
        # # 邮件的发送时间
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        # 读取测试报告的内容
        with open(os.path.join(reportPath, new_report), 'rb') as f:
            mail_body = f.read()
        # 将测试报告的内容放在 邮件的正文当中
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
        # recipients = ['xxxx@xxxx.com', 'xxxx@qq.com', 'xxx@xxxxx.com']  # 发送给多个人
        recipients = ['xxxxx@xxxx.com']  # 发送给一个人
        self.take_messages()
        self.msg['from'] = 'xxxx@xxxx.com'  # 发送邮件的人，这种是公司邮箱转发
        # self.msg['to'] = recipients  # 收件人和发送人必须这里定义一下，执行才不会报错。
        toaddrs = recipients

        smtp = smtplib.SMTP()
        smtp.connect('smtp.xxxx.com')
        smtp.ehlo()
        # 如果发送邮件方是qq邮箱，这里的密码为授权码，而QQ邮箱登录密码
        smtp.login('xxx@xxxx.com', 'xxxxx')
        smtp.sendmail(self.msg['from'], toaddrs, self.msg.as_string())  # 发送邮件
        smtp.close()
        print('sendmail success')


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
