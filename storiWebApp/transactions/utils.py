from django.core import serializers


def send_balance_message(transactions):
    json_transactions = serializers.serialize("json", transactions)
    print(json_transactions)
