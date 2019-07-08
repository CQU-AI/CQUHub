from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import time


content = """
您好:

    感谢您使用CQU Hub！
    为确保论坛只对重大学子开放，请确认您的学号为  {}  ，并使用验证码  {}  来完成您的注册！
    如果您并没有在CQU Hub进行注册，请忽略此邮件。

顺颂 时祺

CQU Hub开发组
{}
"""


def generate_verify_code(student_id):
    res = ""
    code_map = {}
    code = "9128405367"
    for i in range(10):
        code_map[str(i)] = code[i]
    for i in str(hash(str(student_id)) % (3 ** 12)):
        res += code_map[i]
    print('*' * 100, '\n', res, '\n', '*' * 100)
    return res

def validate_code(userInputCode):
    return True

def send_verify_mail(student_id):
    host_server = "smtp.exmail.qq.com"
    pwd = "Djangosucks123"
    sender_mail = "cquhub-no-reply@mail.loopy.tech"
    receiver = "{}@cqu.edu.cn".format(student_id)
    mail_title = "CQU Hub的注册验证"
    mail_content = content.format(
        student_id,
        generate_verify_code(student_id),
        time.strftime("%Y-%m-%d %X", time.localtime()),
    )

    smtp = SMTP_SSL(host_server)

    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_mail, pwd)

    msg = MIMEText(mail_content, "plain", "utf-8")
    msg["Subject"] = Header(mail_title, "utf-8")
    msg["From"] = sender_mail
    msg["To"] = receiver
    smtp.sendmail(sender_mail, receiver, msg.as_string())
    smtp.quit()
