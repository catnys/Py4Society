import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from emailObj import Email

def createMessage(sender, receiver, subject, body):
    # Create the email content
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    # Attach the body text
    message.attach(MIMEText(body, "plain"))
    return message

def main():

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    sender = "<EMAIL>"
    receiver = "<EMAIL>"
    subject = "Motivation Reminder"
    body = "Hello World!"
    password = "<PASSWORD>"
    email = Email(sender, receiver, subject, body,password)
    message = createMessage(sender, receiver, subject, body)

    # Connect to the SMTP server
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls()  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)

        # Send the email
        server.sendmail(email.getSender(), email.getReceiver(), message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()


if __name__ == "__main__":
    main()