# _*_ coding:utf-8 _*_
from datetime import datetime, date
import os
from loguru import logger
import yaml
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import shutil

# 以当前日期创建二级目录，目录格式为2020-03-25
create_directory_date = datetime.now().strftime('%Y-%m-%d')
# 当前时间
currentNow = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


# 创建目录
def create_directory(directory, sub_directory=create_directory_date):
    currentDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), directory, sub_directory)
    try:
        if not os.path.exists(currentDir):
            os.makedirs(currentDir)
            logger.info('目录新建成功:{}', currentDir)
    except OSError as msg:
        logger.info('新建目录失败：', msg)
    return currentDir


# 保存日志文件
def saved_log(name, directory='logs'):
    log_path = create_directory(directory) + '\\' + name + '.txt'
    logger.info(f'当前运行的测试日志文件保存在:{log_path}')
    return log_path


# 保存截图文件
def saved_screenshot(name, directory='screenshot'):
    screenshot_path = create_directory(directory) + '\\' + name + '_' + currentNow + '.png'
    logger.info(f'当前运行的测试用例错误截图保存在：{screenshot_path}')
    return screenshot_path


# 保存测试报告
def saved_report(directory='testReports'):
    report_path = create_directory(directory) + '\\' + currentNow + '_testreport' + '.html'
    logger.info(f'当前测试报告保存在:{report_path}')
    return report_path


# 读取配置文件
def get_yaml_config_file(config_name, directory='config'):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), directory, config_name)
    with open(path, 'r', encoding='utf-8') as f:
        cfg = f.read()
        data = yaml.load(cfg, Loader=yaml.FullLoader)
    return data


# 获取配置文件中的邮箱主机，邮箱用户名和邮箱密码
def get_mail_info():
    data = get_yaml_config_file('config.yaml')
    email_host = data['EMAIL'][0]['EMAIL_HOST']
    email_user = data['EMAIL'][1]['EMAIL_USER']
    email_password = data['EMAIL'][2]['EMAIL_PASSWORD']
    return email_host, email_user, email_password


# 该函数的作用是为了在测试报告的路径下找到最新的测试报告
def get_report():
    report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testReports\\')
    # 列出指定目录下的所有文件和子目录
    dirs = os.listdir(report_path)
    # 把dirs目录下的文件按照创建时间的升序排序
    dirs.sort()
    new_dir = dirs[-1]
    # 获取最新的文件目录
    report = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testReports\\', new_dir + '\\')
    # 获取最新目录中的最新创建的文件
    new_dir = os.listdir(report)
    new_dir.sort()
    # dirs返回是列表，故通过下标去获取最新的报告
    new_report_name = new_dir[-1]
    # 返回最新测试报告的文件名
    return report + new_report_name, report_path


# 该函数的目的是为了准备发送邮件的的消息内容
def take_messages():
    report_path = get_report()[1]
    new_report = get_report()[0]
    msg = MIMEMultipart()
    # 邮件的标题
    email_title = '聊天室脚本运行测试结果'
    msg['Subject'] = f'{email_title}测试报告'
    #  邮件的发送时间
    msg['date'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')
    # 读取最新测试报告的内容
    with open(os.path.join(report_path, new_report), 'rb') as f:
        mail_body = f.read()
    # 将测试报告的内容放在邮件的正文当中
    html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # 将html附加在msg里
    msg.attach(html)
    # 将测试报告放在附件中发送
    att1 = MIMEText(mail_body, 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，附件的名字就是什么
    att1["Content-Disposition"] = f'attachment; filename= "{currentNow}_TestReport.html"'
    msg.attach(att1)
    return msg


# 发送邮件到目标邮箱，测试报告以附件形式发送
def send_mail():
    try:
        # 发送给一个人，也可以发送多个人
        # recipients = ['shift_1220@163.com']
        recipients = ['lidl@cm.mail']
        msg = take_messages()
        # 发送邮件的人
        msg['from'] = get_mail_info()[1]
        toaddrs = recipients
        smtp = smtplib.SMTP()
        smtp.connect(get_mail_info()[0])
        # 如果发送邮件方是qq邮箱，这里的密码为授权码，而非QQ邮箱登录密码
        smtp.login(get_mail_info()[1], get_mail_info()[2])
        smtp.sendmail(msg['from'], toaddrs, msg.as_string())
        smtp.close()
        logger.info('邮件发送成功.....')
    except smtplib.SMTPException:
        logger.error('邮件发送失败，请检查邮件发送配置信息！！')


# 清理logs,testReports,screenshot超过5天目录
def cleanup_directory(directory):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), directory)
    directory_list = os.listdir(path)
    for i in range(len(directory_list)):
        # 当前日期,以（年,月,日）的格式转换为date类型
        now = str(datetime.now().strftime('%Y-%m-%d')).split('-')
        data1 = date(int((now[0])), int(now[1]), int(now[2]))
        timestamp = os.path.getatime(path + '\\' + directory_list[i])
        # 该目录下的子目录创建日期,以（年,月,日）的格式转换为date类型
        time = str(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')).split('-')
        data2 = date(int(time[0]), int(time[1]), int(time[2]))
        # 该目录下的子目录创建日期距离当前日期相差多少天
        delta = (data1 - data2).days
        del_dir = path + '\\' + directory_list[i]
        data = get_yaml_config_file('config.yaml')
        if delta >= data['DAYS']:
            try:
                logger.info('正在执行删除操作........')
                shutil.rmtree(del_dir)
                logger.info('目录删除成功............')
            except FileNotFoundError as msg:
                logger.info(msg)


# 测试用例断言出错写入日志方法
def assertion_error(log_name, case_name, expected_result, actual_result):
    """
    :param log_name: 日志文件名
    :param case_name: 测试用例名称
    :param expected_result: 预期结果
    :param actual_result: 实际结果
    :return:无返回值
    """
    logger.add(saved_log(log_name), encoding='utf-8', level='ERROR')
    logger.error(f'{case_name}，预期结果:{expected_result},实际结果:{actual_result}，实际结果与预期结果不相等，断言失败！！！')
