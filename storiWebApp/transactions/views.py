from datetime import datetime
import pandas as pd

from django.urls import reverse
from django.views.generic import FormView

from .forms import SummaryEmailForm
from .models import Account, Balance, Transaction
from .utils import send_balance_message


class SummaryEmail(FormView):
    template_name = 'summary.html'
    form_class = SummaryEmailForm
    account: Account = None
    balance: Balance = None
    transactions: Transaction = None

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    def form_valid(self, form):
        self.account = self._get_account(form)
        self.account.save()
        self.balance = self._get_balance(self.account, form)
        self.balance.csv_file = form.cleaned_data['csv_file']
        self.balance.save()
        self.transactions = self._process_csv(self.balance.csv_file.url)
        send_balance_message(self.transactions)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse(
            'summary_email',
        )

    def _process_csv(self, url):
        data = pd.read_csv(url, sep=',')
        rows = data.iterrows()
        transactions = [
            Transaction(
                balance=self.balance,
                date=datetime.strptime(f"{row['Date']} 12:00:00", '%Y/%m/%d %H:%M:%S'),
                amount=row['Transaction'],
            )
            for index, row in rows
        ]
        return Transaction.objects.bulk_create(transactions)

    @staticmethod
    def _get_balance(account, form):
        try:
            return Balance.objects.get(
                account=account,
            )
        except Balance.DoesNotExist:
            return Balance(
                account=account,
                csv_file=form.cleaned_data['csv_file'],
            )

    @staticmethod
    def _get_account(form):
        try:
            return Account.objects.get(
                email=form.cleaned_data['email'],
            )
        except Account.DoesNotExist:
            return Account(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
            )
