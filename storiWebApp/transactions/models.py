from django.db import models


def file_generate_upload_path(instance, filename):
    return "files/{file_name}".format(file_name=instance.file_name)


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Account(TimeStampMixin):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return "{email}".format(email=self.email)


class Balance(TimeStampMixin):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='balances',
    )
    csv_file = models.FileField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{account} - {created_at}".format(account=self.account, created_at=self.created_at)


class Transaction(TimeStampMixin):

    balance = models.ForeignKey(
        Balance,
        on_delete=models.CASCADE,
        related_name='transactions',
    )

    date = models.DateTimeField()

    amount = models.FloatField()

    def __str__(self):
        return "{balance} - {amount}".format(balance=self.balance, amount=self.amount)
