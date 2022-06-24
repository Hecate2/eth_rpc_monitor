import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import sys


def send_email(subject: str='测试主题', content: str='测试邮件', smtp_server='smtp.163.com'):
    email_user = os.environ.get('email_user')
    if not email_user:
        print('WARNING: NO email_user specified', file=sys.stderr)
        return 
    password = os.environ.get('password')
    
    email_sender = email_user
    
    receiver = [os.environ.get('receiver', email_user)]
    
    msg = MIMEText(content, 'html', 'utf-8')
    msg['subject'] = Header(subject, 'utf-8')
    msg['From'] = email_sender
    msg['To'] = ','.join(receiver)
    
    print('logging in...')
    smtp = smtplib.SMTP_SSL(smtp_server, 465)
    smtp.helo(smtp_server)
    smtp.ehlo(smtp_server)
    smtp.login(email_user, password)
    
    print("Sending email....")
    smtp.sendmail(email_sender, receiver, msg.as_string())
    smtp.quit()
    print("Email sent")


if __name__ == '__main__':
    send_email()