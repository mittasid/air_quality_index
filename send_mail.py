#Code to send email using smtp.gmai.com

import smtplib, ssl
import config

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = config.sender_email  # Enter your address
receiver_email = "mittasid@gmail.com"  # Enter receiver address

password = config.email_password

# Create a secure SSL context
context = ssl.create_default_context()

def send_email(message):
    print(message)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
