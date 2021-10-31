import smtplib
from email.mime.text import MIMEText

from config import password, rules


# from locale_config import MAILTRAP_APIKEY

def send_smtp_email(subject, body):
    sender = "enter email sender"
    receiver = rules["email"]["receiver"]

    message = MIMEText(body)
    message["subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("api", password)
        server.sendmail(sender, receiver, message.as_string())