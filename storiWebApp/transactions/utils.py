import json
import logging
import os
import boto3
import calendar
from datetime import datetime


def enqueue(message_body):
    client = boto3.client(
        'sqs',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION_NAME'),
    )
    queue_url = os.getenv('SEND_BALANCE_QUEUE_URL')

    return client.send_message(
        QueueUrl=queue_url, MessageBody=json.dumps(message_body),
    )


def send_balance_message(transactions):
    total_balance: float = 0
    debit_amount: float = 0
    credit_amount: float = 0
    months: set = set()
    trans_per_month: list = []
    rows = transactions.iterrows()

    for index, row in rows:
        total_balance += row['Transaction']
        date = datetime.strptime(f"{row['Date']} 12:00:00", '%Y/%m/%d %H:%M:%S')
        trans_per_month.append(calendar.month_name[date.month])
        months.add(calendar.month_name[date.month])
        if row['Transaction'] > 0:
            credit_amount += row['Transaction']
        else:
            debit_amount += row['Transaction']

    balance_data = {
        'total_balance': total_balance,
        'credit_amount': credit_amount,
        'debit_amount': debit_amount
    }

    for month in months:
        balance_data.update({f'transactions_in_{month}': trans_per_month.count(month)})

    try:
        enqueue(balance_data)
    except Exception as error:
        logger = logging.getLogger('django')
        logger.error(error)
