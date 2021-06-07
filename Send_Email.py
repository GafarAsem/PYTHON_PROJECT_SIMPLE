import smtplib
from mailer import Mailer
from mailer import Message

gmail_user = 'gmail_user@gmail.com'
gmail_password = 'gmail_password'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail('gmail_user@gmail.com', 'gmail_user@gmail.com', "Hello")
server.close()
