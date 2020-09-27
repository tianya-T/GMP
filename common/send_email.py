# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# Author: LiYangYang            # Date: 2020 年
# Description:
# -----------------------------------------------------------------------------------

import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.get_data import GetYamlData
from common.get_path import GetPath


class SendEmail:

    def send_email(self, report_path):
        """
        发送邮件
        :param report_path:附件地址
        :return:
        """
        global smtp

        __PATH = GetPath().get_path('gmp\\common\\BOXconfig.yaml')  # 获取配置文件地址
        __CONFIG = GetYamlData().get_yaml_data(__PATH)['SendEmail']  # 获取配置文件内容

        smtpserver = __CONFIG['SMTPSERVER']  # 设置邮箱服务器与端口
        port = __CONFIG['PORT']
        sender = __CONFIG['SENDER']  # 发件人
        pwd = __CONFIG['PWD']  # 授权码
        receiver = __CONFIG['receiver']  # 收件人

        msg = MIMEMultipart()
        msg['from'] = sender  # 填写发件人
        msg['to'] = receiver  # 填写收件人
        msg['subject'] = 'test'  # 主题
        with open(report_path, 'rb') as f:  # 打开附件并读取内容
            data = f.read()
        report_text = MIMEText(data, 'html', 'utf8')  # 写入邮件内容
        msg.attach(report_text)
        att = MIMEText(data, 'base64', 'utf8')  # 添加附件
        att['Content-Type'] = 'application/octet-stream'  # 需要添加附件,设置type
        att['Content-Disposition'] = 'attachment;filename = %s' % report_path
        msg.attach(att)

        smtp = smtplib.SMTP()  # 实例化邮件服务器对象
        try:
            smtp.connect(smtpserver, port)  # 连接服务器
        except Exception as contE:
            print(contE, '服务器连接失败..')
            sys.exit()

        try:
            smtp.login(sender, pwd)  # 登录
        except Exception as loginE:
            print(loginE, '账号或者密码错误')
            sys.exit()

        try:
            smtp.sendmail(sender, receiver.split(','), msg.as_string())  # 发送邮件
            smtp.close()  # 关闭链接
            print('邮件发送完成')
        except Exception as sendE:
            print(sendE, '发送失败,邮箱设置错误')
            sys.exit()


if __name__ == '__main__':
    send = SendEmail()
    send.send_email(r"D:\Users\C0600\Desktop\Tian\PW.txt")
