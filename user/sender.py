from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import time, random


class Sender:
    sender_cache = {}

    def __init__(self, id, debug=False):
        self.content = """
        您好:

            感谢您使用CQU Hub！
            为确保论坛只对重大学子开放，请确认您的学号为  {}  ，并使用验证码  {}  来完成您的注册！
            如果您并没有在CQU Hub进行注册，请忽略此邮件。

        顺颂 时祺

        CQU Hub开发组
        {}
        """
        self.student_id = id
        self.debug = debug

    def generate_token(self):
        token = ""
        for i in range(6):
            token += str(random.randint(0, 9))
            self.sender_cache[self.student_id] = [token, time.time()]
        return token

    def validate_code(self, userInputCode):
        for id in list(self.sender_cache.keys()):
            if self.sender_cache[id][1] - time.time() > 3600:
                del self.sender_cache[id]
        print(self.sender_cache)
        return self.student_id in self.sender_cache.keys() and self.sender_cache[self.student_id][0] == userInputCode

    def send_verify_mail(self):
        if self.debug:
            print("*" * 79 + "\n" + str(self.generate_token()) + "\n" + "*" * 79)
            return
        host_server = "smtp.exmail.qq.com"
        pwd = "Djangosucks123"
        sender_mail = "cquhub-no-reply@mail.loopy.tech"
        receiver = "{}@cqu.edu.cn".format(self.student_id)
        mail_title = "CQU Hub的注册验证"
        mail_content = self.content.format(
            self.student_id,
            self.generate_token(),
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
