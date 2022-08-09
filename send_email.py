from config import MAIL_HOST, MAIL_PORT, MAIL_ADDRESS, MAIL_PASSWORD
from markdown import markdown
from datetime import datetime

import smtplib
import ssl

from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_test_mail(recipients):
    """Send test mail to one or a list of recipients
    Does not work for mail aliases 
    """
    # Get current time for the subject of the mail
    current_time_string = datetime.now().strftime('%H:%M:%S')

    # Setup the msg object
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Mail ' + current_time_string
    msg['From'] = MAIL_ADDRESS 
    # msg['To'] must be str()
    msg['To'] = ",".join(recipients) if isinstance(recipients, list) \
    else recipients

    # Create content for the message
    text_file = './textfile'
    with open(text_file, 'r') as fp:
        text = fp.read() 
        
    formatted_file = './formatted'
    with open(formatted_file, 'r') as fp:
        html = fp.read()

    part1 = MIMEText(text, 'plain')     
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # Setup the server
    server = smtplib.SMTP(MAIL_HOST, MAIL_PORT)
    context = ssl.create_default_context()
    # start TLS for security
    # server.ehlo()
    server.starttls(context=context)
    # server.ehlo()
    # Authentication
    server.login(MAIL_ADDRESS, MAIL_PASSWORD)
    # Sen
    # server.send_message(msg=msg)
    server.sendmail(msg['From'], recipients, msg.as_string())
    server.quit()


def send_batch_test_mail(emails_list):
    """Works for aliases, but slow
    """
    for email in emails_list:
        try:
            send_test_mail(email)
            print(f"{email} sent")
        except Exception as ex:
            print(f"Can't send to {email}:\n{ex}")
