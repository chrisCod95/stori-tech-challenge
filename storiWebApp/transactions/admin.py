from django.contrib import admin
from .models import Account, Balance, Transaction


admin.site.register(Account)
admin.site.register(Balance)
admin.site.register(Transaction)
