import os
import smtplib
import ssl
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .utils import build_html


def send_balance_email(event, context):
    records = event['Records']
    for record in records:
        event_body = json.loads(record['body'])

        email_sender = 'info.hazblon@gmail.com'
        email_password = os.getenv('EMAIL_PASSWORD')
        email_receiver = event_body['account']['email']

        text = "Hello Dear Storian. Here you are your asked account balance"
        html = build_html(event_body['data'], event_body['account']['name'])
        text_part = MIMEText(text, "plain")
        html_part = MIMEText(html, "html")

        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Stori Balance"
        message["From"] = email_sender
        message["To"] = email_receiver
        message.attach(text_part)
        message.attach(html_part)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, message.as_string())
        except Exception as e:
            return e
