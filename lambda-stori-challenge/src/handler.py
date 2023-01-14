import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .utils import build_html


def send_balance_email(event, context):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    smtp_user = '649bb5b78a38d6'
    password = '5b439784937d14'

    sender_email = 'service.client@stori.com'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Your Stori Balance"
    message["From"] = sender_email

    records = event['Records']

    for record in records:
        event_body = json.loads(record['body'])
        reciever_email = event_body['account']['email']
        message["To"] = reciever_email

        text = "Hello Dear Storian. Here you are your asked account balance"
        html = build_html(event_body['data'], event_body['account']['name'])

        text_part = MIMEText(text, "plain")
        html_part = MIMEText(html, "html")
        message.attach(text_part)
        message.attach(html_part)

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.login(smtp_user, password)
                return server.sendmail(
                    sender_email,
                    reciever_email,
                    message.as_string()
                )
        except Exception as error:
            return error
