import os
from dotenv import load_dotenv
from markdown import markdown

# Import smtplib for the actual sending function
import smtplib
import ssl

# Import the email modules we'll need
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
password = os.getenv('GMAIL_PASSWORD')
sender = os.getenv('GMAIL_ADDRESS')


def send_gmail(recipient):
    # Create mail
    textfile = './textfile.txt'

    with open(textfile, 'rb') as fp:
        msg = EmailMessage()
        content = fp.read()
        msg.set_content(content, 'text', 'plain')

    msg['Subject'] = "Simple text mail"
    msg['From'] = sender
    msg['To'] = recipient 

    # Setup the server
    s = smtplib.SMTP("smtp.gmail.com", 587)
    context = ssl.create_default_context()
    # start TLS for security
    s.starttls(context=context)
    # Authentication
    s.login(sender, password)
    # Send
    s.send_message(msg=msg)
    s.quit()


def send_fancy_mail(recipient):
    # Setup the msg object
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Formatted mail'
    msg['From'] = sender
    msg['To'] = recipient

    # Create content for the message
    textfile = './textfile.txt'
    with open(textfile, 'r') as fp:
        text = fp.read() 
        
    formatted_file = './Notes for using Linux.md'
    with open(formatted_file, 'r') as fp:
        html = markdown(fp.read())

    part1 = MIMEText(text, 'plain')     
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    print(msg)

    # Setup the server
    s = smtplib.SMTP("smtp.gmail.com", 587)
    context = ssl.create_default_context()
    # start TLS for security
    s.starttls(context=context)
    # Authentication
    s.login(sender, password)
    # Send
    s.send_message(msg=msg)
    s.quit()

