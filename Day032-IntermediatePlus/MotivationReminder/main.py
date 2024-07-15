import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def createMessage(sender, receiver, subject, body):
    # Create the email content
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    # Attach the body text
    message.attach(MIMEText(body, "plain"))
    return message
