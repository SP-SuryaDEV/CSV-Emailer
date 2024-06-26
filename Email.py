import smtplib
from email.message import EmailMessage

class Emailer:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send(self, recipient, subject, body):
        msg = EmailMessage()
        msg['From'] = self.email
        msg['To'] = recipient
        msg['Subject'] = subject  
        msg.set_content(body)

        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', st.sectrets['PORT'])
        smtp_server.login(self.email, self.password)
        smtp_server.send_message(msg)
        smtp_server.quit()


class SendEmail:

    def __init__(self, email, subject):
        self.emailer = Emailer(st.secrets['EMAIL'], st.secrets['PASS_KEY'])
        self.receiver = email
        self.subject = subject

    def sendMessage(self, message):
        self.emailer.send(self.receiver, self.subject, message)
